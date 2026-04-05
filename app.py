import streamlit as st

# Function
def generate_learning_path(topic, level):
    topic = topic.lower()

    if "machine learning" in topic:
        if level == "Beginner":
            return [
                "📘 Learn Python Basics",
                "📊 Learn NumPy & Pandas",
                "📈 Basics of Statistics"
            ]
        elif level == "Intermediate":
            return [
                "🤖 Learn ML Algorithms",
                "📊 Work with datasets",
                "🧠 Build ML models"
            ]
        else:
            return [
                "🚀 Deep Learning",
                "🧠 Neural Networks",
                "📦 Deploy ML Models"
            ]

    elif "web development" in topic:
        return [
            "🌐 HTML, CSS",
            "⚡ JavaScript",
            "⚛️ React",
            "🖥️ Backend Development",
            "📦 Full Stack Projects"
        ]

    return [
        "📌 Learn Basics",
        "📌 Practice",
        "📌 Build Projects"
    ]


# UI
st.set_page_config(page_title="AI Learning Path Generator", page_icon="🤖")

st.title("🤖 AI Learning Path Generator")
st.write("Create a personalized roadmap with AI 🚀")

# Inputs
topic = st.text_input("Enter Topic:")
level = st.selectbox("Select Difficulty Level:", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Learning Path"):
    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic")
    else:
        path = generate_learning_path(topic, level)

        st.subheader("📚 Your Learning Path:")
        for step in path:
            st.write(step)

        # Resources
        st.subheader("📺 Recommended Resources:")
        st.write("- YouTube: Free tutorials")
        st.write("- Coursera / Udemy courses")
        st.write("- Practice on Kaggle / LeetCode")

        # Download button
        text = "\n".join(path)
        st.download_button("📥 Download Plan", text, file_name="learning_path.txt")

        st.success("✅ Generated Successfully!")