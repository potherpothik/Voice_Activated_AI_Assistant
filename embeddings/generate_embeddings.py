import pickle
import os
import json
import numpy as np
import requests
import sys
sys.path.append('..')
from config import OLLAMA_HOST, EMBEDDING_MODEL, SERVICES


class ServiceEmbeddings:
    def __init__(self):
        self.embedding_model = EMBEDDING_MODEL
        self.ollama_host = OLLAMA_HOST
        self.services = SERVICES
        self.embeddings = {}
        self.storage_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'service_store.pkl')

    def generate_embedding(self, text: str) -> list:
        """Generate embedding for a given text using Ollama."""
        response = requests.post(
            f"{self.ollama_host}/api/embeddings",
            json={"model": self.embedding_model, "prompt": text}
        )
        
        if response.status_code == 200:
            return response.json()["embedding"]
        else:
            print(f"Error generating embedding: {response.text}")
            return []

    def generate_service_embeddings(self):
        """Generate embeddings for all services."""
        for service_id, service_info in self.services.items():
            # Create a comprehensive text representation of the service
            service_text = f"{service_info['name']}. {service_info['description']} Common issues: {', '.join(service_info['common_issues'])}"
            
            # Generate embedding
            embedding = self.generate_embedding(service_text)
            
            if embedding:
                self.embeddings[service_id] = {
                    "embedding": embedding,
                    "info": service_info
                }
        
        # Save embeddings to file
        self.save_embeddings()

    def save_embeddings(self):
        """Save embeddings to a pickle file."""
        with open(self.storage_path, 'wb') as f:
            pickle.dump(self.embeddings, f)
        print(f"Embeddings saved to {self.storage_path}")

    def load_embeddings(self):
        """Load embeddings from a pickle file."""
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'rb') as f:
                self.embeddings = pickle.load(f)
            print(f"Embeddings loaded from {self.storage_path}")
            return True
        return False

    def find_most_similar_service(self, query: str) -> tuple:
        """Find the most similar service to a query."""
        query_embedding = self.generate_embedding(query)
        
        if not query_embedding:
            return None, 0
        
        best_match = None
        highest_similarity = -1
        
        for service_id, service_data in self.embeddings.items():
            service_embedding = service_data["embedding"]
            
            # Calculate cosine similarity
            similarity = self._cosine_similarity(query_embedding, service_embedding)
            
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = service_id
        
        return best_match, highest_similarity

    def _cosine_similarity(self, vec1, vec2):
        """Calculate cosine similarity between two vectors."""
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


if __name__ == "__main__":
    # Generate and save embeddings when run directly
    embeddings = ServiceEmbeddings()
    embeddings.generate_service_embeddings()
