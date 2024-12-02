from flask import Flask, render_template, jsonify

app = Flask(__name__)

Job = [
    {
        "job_title": "Python Developer",
        "company": "Tech Solutions Inc.",
        "location": "New York, NY",
        "salary_range": "$70,000 - $90,000",
        "employment_type": "Full-time",
        "experience_level": "Entry-level",
        "required_skills": ["Python", "Flask", "Django", "SQL", "Git"],
        "job_description": "Develop and maintain backend services using Python. Collaborate with frontend developers to integrate APIs.",
    },
    {
        "job_title": "Cloud Engineer",
        "company": "CloudNext",
        "location": "San Francisco, CA",
        "salary_range": "$85,000 - $110,000",
        "employment_type": "Full-time",
        "experience_level": "Mid-level",
        "required_skills": ["AWS", "Azure", "Docker", "Kubernetes", "CI/CD"],
        "job_description": "Design and implement scalable cloud infrastructure. Automate cloud services deployment using industry best practices.",
    },
    {
        "job_title": "Data Analyst",
        "company": "Insight Analytics",
        "location": "Remote",
        "salary_range": "$60,000 - $80,000",
        "employment_type": "Full-time",
        "experience_level": "Entry-level",
        "required_skills": ["SQL", "Excel", "Python", "Power BI", "Tableau"],
        "job_description": "Analyze business data and provide actionable insights. Create dashboards and reports to support decision-making.",
    },
    {
        "job_title": "UI/UX Designer",
        "company": "Creative Minds",
        "location": "Austin, TX",
        "salary_range": "$65,000 - $85,000",
        "employment_type": "Full-time",
        "experience_level": "Mid-level",
        "required_skills": ["Adobe XD", "Figma", "HTML", "CSS", "JavaScript"],
        "job_description": "Design user interfaces and experiences for web and mobile applications. Conduct user research and usability testing.",
    },
    {
        "job_title": "DevOps Engineer",
        "company": "Tech Innovators",
        "location": "Seattle, WA",
        "salary_range": "$90,000 - $120,000",
        "employment_type": "Full-time",
        "experience_level": "Senior-level",
        "required_skills": ["Linux", "AWS", "Terraform", "Jenkins", "Bash/Shell"],
        "job_description": "Implement DevOps practices to streamline software development. Automate infrastructure and CI/CD pipelines.",
    },
]


@app.route("/")
def home():
    return render_template("Home.html", jobs_data=Job)


@app.route("/jobs")
def list_jobs():
    return jsonify(Job)


if __name__ == "__main__":
    app.run(debug=True)
