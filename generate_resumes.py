import os
import random
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Output directory setup
output_dir = "resume"
os.makedirs(output_dir, exist_ok=True)

# Pick 5 random resume indices out of 50 to focus on Agentic AI & RAG
agentic_ai_resume_indices = set(random.sample(range(1, 51), 5))

# standard pools
first_names = [
    "Alex", "Jordan", "Taylor", "Morgan", "Sam", "Chris", "Pat", "Riley",
    "Dakota", "Avery", "Cameron", "Quinn", "Skyler", "Jesse", "Reese",
    "Casey", "Jamie", "Peyton", "Kendall", "Hayden"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
    "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

standard_roles = [
    "Full Stack Developer", "Backend Engineer", "Frontend Developer",
    "DevOps Engineer", "Software Engineer", "Cloud Architect",
    "Mobile App Developer (iOS/Android)", "Data Engineer", "Site Reliability Engineer"
]

standard_tech_skills = [
    "Python", "JavaScript", "TypeScript", "React", "Node.js", "Java",
    "C++", "Go", "Docker", "Kubernetes", "AWS", "PostgreSQL",
    "MongoDB", "REST APIs", "CI/CD", "Git", "Redis"
]

# Agentic AI & RAG specific pools
ai_roles = [
    "Agentic AI Engineer", "LLM & RAG Solutions Architect",
    "Generative AI Engineer", "AI Systems & Agents Developer"
]

ai_skills = [
    "Agentic AI Workflows", "RAG (Retrieval-Augmented Generation)", "LangChain / LangGraph",
    "LlamaIndex", "Vector DBs (Pinecone, Chroma, Qdrant)", "CrewAI / AutoGen",
    "OpenAI API / Function Calling", "Fine-Tuning LLMs", "Semantic Search",
    "Python", "Docker", "FastAPI", "PostgreSQL (pgvector)"
]

cities = ["San Francisco, CA", "Seattle, WA", "New York, NY", "Austin, TX", "Chicago, IL", "Boston, MA"]

def generate_pdf(file_path, name, role, is_agentic_ai):
    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'NameTitle',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#1A202C')
    )
    subtitle_style = ParagraphStyle(
        'RoleSubtitle',
        parent=styles['Heading2'],
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#2B6CB0')
    )
    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading3'],
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#2D3748'),
        spaceBefore=8,
        spaceAfter=3
    )
    body_style = ParagraphStyle(
        'BodyCustom',
        parent=styles['Normal'],
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#4A5568')
    )

    story = []

    # Header section
    story.append(Paragraph(f"<b>{name}</b>", title_style))
    story.append(Paragraph(f"<b>{role}</b>", subtitle_style))
    
    email = f"{name.lower().replace(' ', '.')}@example.com"
    phone = f"+1 (555) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
    city = random.choice(cities)
    story.append(Paragraph(f"Email: {email} | Phone: {phone} | Location: {city}", body_style))
    story.append(Spacer(1, 8))

    # Summary
    story.append(Paragraph("<b>PROFESSIONAL SUMMARY</b>", heading_style))
    exp_years = random.randint(3, 7)
    
    if is_agentic_ai:
        summary_text = (
            f"Specialized {role} with {exp_years}+ years of experience architecting autonomous AI agents "
            f"and production RAG (Retrieval-Augmented Generation) systems. Proven expertise in building end-to-end "
            f"LLM pipelines, implementing multi-agent orchestration, and optimizing vector database retrieval."
        )
    else:
        summary_text = (
            f"Results-oriented {role} with {exp_years}+ years of experience building and optimizing "
            f"scalable applications. Skilled in modern software architecture, writing clean maintainable code, "
            f"and implementing CI/CD pipelines in Agile environments."
        )
    
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 6))

    # Skills
    story.append(Paragraph("<b>TECHNICAL SKILLS</b>", heading_style))
    if is_agentic_ai:
        selected_skills = random.sample(ai_skills, k=8)
    else:
        selected_skills = random.sample(standard_tech_skills, k=8)
        
    story.append(Paragraph(f"<b>Technologies:</b> {', '.join(selected_skills)}", body_style))
    story.append(Spacer(1, 6))

    # Experience
    story.append(Paragraph("<b>WORK EXPERIENCE</b>", heading_style))
    
    company1 = f"NextGen AI {random.choice(['Labs', 'Systems', 'Tech'])}" if is_agentic_ai else f"Tech Solutions {random.choice(['Inc.', 'Corp', 'Labs'])}"
    story.append(Paragraph(f"<b>{role}</b> — {company1}", body_style))
    story.append(Paragraph("<i>2022 – Present</i>", body_style))
    
    if is_agentic_ai:
        story.append(Paragraph("• Designed multi-agent workflows using LangGraph and CrewAI for complex automated decision-making.", body_style))
        story.append(Paragraph("• Implemented high-precision RAG pipelines using LlamaIndex and Pinecone vector store, reducing LLM hallucinations by 40%.", body_style))
        story.append(Paragraph("• Integrated function-calling and external tools to build context-aware AI assistants for enterprise clients.", body_style))
    else:
        story.append(Paragraph(f"• Designed and implemented microservices using {selected_skills[0]} and {selected_skills[1]}.", body_style))
        story.append(Paragraph(f"• Reduced API latency by {random.randint(15, 45)}% through code refactoring and database query optimization.", body_style))
        story.append(Paragraph("• Collaborated with product teams to define technical requirements and deliver sprint goals.", body_style))
    
    story.append(Spacer(1, 6))

    # Previous Job
    company2 = f"Cloud Innovators {random.choice(['LLC', 'Group'])}"
    story.append(Paragraph(f"<b>Software Engineer</b> — {company2}", body_style))
    story.append(Paragraph("<i>2020 – 2022</i>", body_style))
    
    if is_agentic_ai:
        story.append(Paragraph("• Built hybrid search pipelines combining keyword BM25 and semantic vector search.", body_style))
        story.append(Paragraph("• Fine-tuned open-source LLMs on proprietary domain data to improve accuracy.", body_style))
    else:
        story.append(Paragraph(f"• Developed full-stack features utilizing {selected_skills[2]} and cloud services.", body_style))
        story.append(Paragraph("• Automated testing suites, improving test coverage by 30%.", body_style))
        
    story.append(Spacer(1, 6))

    # Education
    story.append(Paragraph("<b>EDUCATION</b>", heading_style))
    story.append(Paragraph("<b>B.S. in Computer Science</b> — State University", body_style))

    doc.build(story)

# Generate 50 PDF Resumes
for i in range(1, 51):
    first = random.choice(first_names)
    last = random.choice(last_names)
    full_name = f"{first} {last}"
    
    is_agentic_ai = i in agentic_ai_resume_indices
    role = random.choice(ai_roles) if is_agentic_ai else random.choice(standard_roles)
    
    tag = "_AGENTIC_AI_RAG" if is_agentic_ai else ""
    file_name = f"resume_{i:02d}_{first}_{last}{tag}.pdf"
    file_path = os.path.join(output_dir, file_name)
    
    generate_pdf(file_path, full_name, role, is_agentic_ai)
    
    label = " [AGENTIC AI & RAG SPECIALIST]" if is_agentic_ai else ""
    print(f"[{i}/50] Generated: {file_path}{label}")

print(f"\nDone! Exactly 5 resumes were created with Agentic AI & RAG focus (indices: {sorted(list(agentic_ai_resume_indices))}).")