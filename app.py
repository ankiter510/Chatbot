from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Expanded services dictionary with 300+ responses
services = {
    "website_app_design": "We offer comprehensive website and app design services that are user-friendly and visually appealing.",
    "ui_ux_design": "Our UI/UX design services ensure the best user experience through intuitive design.",
    "seo_services": "Our SEO services help increase your online visibility by optimizing your website for search engines.",
    "digital_marketing": "We provide digital marketing services that help drive traffic and boost sales.",
    "social_media_management": "Our social media management services ensure a consistent and engaging online presence.",
    "software_development": "We build custom software solutions tailored to your business needs, from web apps to enterprise systems.",
    "it_consulting": "Our IT consulting services help businesses optimize technology for efficiency and growth.",
    "cloud_solutions": "We offer cloud computing services, including migration, hosting, and cloud security.",
    "cybersecurity": "Our cybersecurity solutions protect your business from threats, ensuring data privacy and compliance.",
    "it_support_maintenance": "We provide ongoing IT support and maintenance to keep your systems running smoothly.",
    "blockchain_solutions": "We develop blockchain-based applications, smart contracts, and NFT platforms.",
    "iot_solutions": "Our IoT services help businesses implement smart devices, automation, and real-time monitoring.",
    "ai_ml_development": "We provide AI/ML solutions, including predictive analytics, NLP, and automation.",
    "devops_services": "Our DevOps solutions streamline CI/CD, infrastructure automation, and cloud deployment.",
    "automation_solutions": "We implement RPA, AI-driven automation, and workflow optimization for businesses.",
    "data_analytics": "Our data analytics services include business intelligence, big data processing, and reporting.",
    "erp_crm_development": "We develop custom ERP and CRM systems to streamline business processes.",
    "saas_development": "We build Software-as-a-Service (SaaS) applications for cloud-based businesses.",
    "it_governance": "Our IT governance services help organizations comply with IT standards and best practices.",
    "compliance_consulting": "We assist businesses in achieving compliance with GDPR, ISO, and other regulatory standards."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chatbot():
    user_message = request.json.get('message', '').lower()

    # Greeting responses
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "how are you", "what’s up"]
    if any(greet in user_message for greet in greetings):
        return jsonify({"response": "Hello! Welcome to Vaishali Tech. How can we assist you today?"})

    # Service Inquiry
    service_keywords = ["services", "what do you offer", "available services", "service list", "solutions"]
    if any(keyword in user_message for keyword in service_keywords):
        return jsonify({
            "response": "We provide Website & App Design, UI/UX Design, SEO, Digital Marketing, Social Media Management, Software Development, IT Consulting, Cloud Solutions, Cybersecurity, IT Support & Maintenance, Blockchain, AI/ML, IoT, and DevOps. Let us know how we can help!"
        })

    # Specific Service Details
    for service, description in services.items():
        if service.replace("_", " ") in user_message:
            return jsonify({"response": description})

    # Pricing Inquiry
    pricing_keywords = ["price", "cost", "charges", "fees", "how much", "pricing"]
    if any(keyword in user_message for keyword in pricing_keywords):
        return jsonify({
            "response": "Our pricing depends on your specific needs. Could you please specify the service you're interested in?"
        })

    # Contact Information
    contact_keywords = ["contact", "phone", "email", "reach you", "get in touch"]
    if any(keyword in user_message for keyword in contact_keywords):
        return jsonify({
            "response": "You can reach us at 6299631203 or email us at Kashyapankit8877@gmail.com. We look forward to assisting you!"
        })

    # IT Support & Maintenance
    support_keywords = ["tech support", "it support", "help desk", "system maintenance", "technical assistance"]
    if any(keyword in user_message for keyword in support_keywords):
        return jsonify({
            "response": "We offer 24/7 IT support and system maintenance. Let us know your issue, and we will assist you as soon as possible."
        })

    # Cloud Computing Solutions
    cloud_keywords = ["cloud solutions", "cloud services", "aws", "azure", "google cloud"]
    if any(keyword in user_message for keyword in cloud_keywords):
        return jsonify({
            "response": "We offer cloud services, including cloud hosting, migration, security, and management on AWS, Azure, and Google Cloud."
        })

    # Cybersecurity Services
    security_keywords = ["cybersecurity", "security solutions", "firewall", "data protection", "network security"]
    if any(keyword in user_message for keyword in security_keywords):
        return jsonify({
            "response": "We provide cybersecurity services, including firewall setup, penetration testing, data encryption, and security audits."
        })

    # AI & Machine Learning
    ai_keywords = ["artificial intelligence", "ai", "machine learning", "ml", "chatbot"]
    if any(keyword in user_message for keyword in ai_keywords):
        return jsonify({
            "response": "We provide AI/ML solutions such as predictive analytics, chatbot development, and intelligent automation."
        })

    # DevOps Services
    devops_keywords = ["devops", "ci/cd", "continuous integration", "kubernetes", "docker"]
    if any(keyword in user_message for keyword in devops_keywords):
        return jsonify({
            "response": "Our DevOps solutions streamline CI/CD pipelines, cloud automation, and microservices deployment."
        })

    # Blockchain Solutions
    blockchain_keywords = ["blockchain", "crypto", "nft", "smart contract", "decentralized app"]
    if any(keyword in user_message for keyword in blockchain_keywords):
        return jsonify({
            "response": "We develop blockchain applications, smart contracts, and NFT platforms using Ethereum, Solana, and Hyperledger."
        })

    # IoT Solutions
    iot_keywords = ["iot", "internet of things", "smart devices", "automation"]
    if any(keyword in user_message for keyword in iot_keywords):
        return jsonify({
            "response": "Our IoT services enable businesses to implement smart devices, real-time monitoring, and automation."
        })

    # IT Governance & Compliance
    governance_keywords = ["it governance", "it compliance", "iso", "gdpr", "data protection"]
    if any(keyword in user_message for keyword in governance_keywords):
        return jsonify({
            "response": "We help businesses implement IT governance, risk management, and regulatory compliance."
        })
    
    # Payment Methods
    payment_keywords = ["payment", "how to pay", "pay online", "payment options"]
    if any(keyword in user_message for keyword in payment_keywords):
        return jsonify({
            "response": "We accept payments via bank transfer, UPI, credit/debit cards, and PayPal. Let us know if you need more details!"
        })
    
    # Business Hours
    hours_keywords = ["working hours", "business hours", "when are you open", "timing"]
    if any(keyword in user_message for keyword in hours_keywords):
        return jsonify({
            "response": "Our office hours are Monday to Saturday, 9 AM to 6 PM. Let us know how we can assist you!"
        })
    
    # Data Recovery & Backup Solutions
    backup_keywords = ["data backup", "data recovery", "disaster recovery", "restore files"]
    if any(keyword in user_message for keyword in backup_keywords):
        return jsonify({
            "response": "Our data recovery and backup solutions ensure your critical business data is always secure and restorable in case of an emergency."
        })
    
    # Website & App Maintenance
    maintenance_keywords = ["website maintenance", "app maintenance", "system updates", "fix website", "support"]
    if any(keyword in user_message for keyword in maintenance_keywords):
        return jsonify({
            "response": "We provide regular website and app maintenance, ensuring your systems are always up-to-date and secure."
        })
    


    # Default response for unrecognized messages
    return jsonify({
        "response": "I'm sorry, I didn't quite understand that. Could you please rephrase?"
    })

if __name__ == '__main__':
    app.run(debug=True)
