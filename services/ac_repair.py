from typing import Dict, List, Any


class ACRepairService:
    def __init__(self):
        self.service_info = {
            "name": "Air Conditioning Repair",
            "description": "Repair and maintenance services for AC units including cooling issues, strange noises, water leakage, and thermostat problems.",
            "common_issues": ["not cooling", "strange noises", "water leakage", "thermostat issues", "blowing warm air"],
            "price_range": "$80-$300"
        }
        self.diagnostic_questions = [
            "What is the make and model of your AC unit?",
            "When did you first notice the issue?",
            "Have you tried any troubleshooting steps already?",
            "Is the AC making any unusual noises?",
            "Is your AC turning on but not cooling properly?"
        ]
    
    def get_response(self, issue_description: str) -> Dict[str, Any]:
        """
        Generate a response based on the AC issue description.
        """
        # Determine which common issue this most closely matches
        matched_issue = self._match_issue(issue_description)
        
        response = {
            "service_type": "ac_repair",
            "matched_issue": matched_issue,
            "response_text": self._generate_response_for_issue(matched_issue, issue_description),
            "follow_up_question": self._get_relevant_diagnostic_question(matched_issue)
        }
        
        return response
    
    def _match_issue(self, issue_description: str) -> str:
        """
        Match the issue description to one of the common issues.
        """
        issue_lower = issue_description.lower()
        
        # Simple keyword matching
        if "not cooling" in issue_lower or "warm air" in issue_lower or "hot air" in issue_lower:
            return "not cooling"
        elif "noise" in issue_lower or "loud" in issue_lower or "sound" in issue_lower:
            return "strange noises"
        elif "water" in issue_lower or "leak" in issue_lower or "dripping" in issue_lower:
            return "water leakage"
        elif "thermostat" in issue_lower or "temperature" in issue_lower or "setting" in issue_lower:
            return "thermostat issues"
        else:
            return "general issue"
    
    def _generate_response_for_issue(self, issue_type: str, issue_description: str) -> str:
        """
        Generate a response based on the type of issue.
        """
        responses = {
            "not cooling": "I understand your AC is not cooling properly. This could be due to a refrigerant leak, dirty condenser coils, or a faulty compressor. Our technician can diagnose and fix this issue quickly.",
            "strange noises": "Unusual noises from your AC could indicate a loose component, a failing motor bearing, or debris in the system. Our technician will identify the source of the noise and resolve it.",
            "water leakage": "Water leakage is often caused by a clogged condensate drain line or a frozen evaporator coil. We can clean the drain line and check for other potential causes.",
            "thermostat issues": "Problems with the thermostat can prevent your AC from functioning correctly. We can test your thermostat and replace it if necessary.",
            "general issue": "Based on your description, we'll need a technician to examine your AC unit to determine the exact issue. We provide comprehensive AC repair services for all types of problems."
        }
        
        return responses.get(issue_type, responses["general issue"])
    
    def _get_relevant_diagnostic_question(self, issue_type: str) -> str:
        """
        Return a relevant diagnostic question based on the issue type.
        """
        questions = {
            "not cooling": "When was the last time you replaced or cleaned your AC filters?",
            "strange noises": "Can you describe the noise? Is it a buzzing, grinding, or rattling sound?",
            "water leakage": "Where exactly is the water leaking from?",
            "thermostat issues": "Does your thermostat display the correct temperature?",
            "general issue": "What is the make and model of your AC unit?"
        }
        
        return questions.get(issue_type, self.diagnostic_questions[0])
