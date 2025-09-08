import streamlit as st

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.title("📝 To-Do List App")

task = st.text_input("Add a new task")

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append(task)
        st.success("Task added!")
    else:
        st.error("Please enter a task.")

st.subheader("Your Tasks")

for i, t in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([8,1])
    with col1:
        st.write(f"{i+1}. {t}")
    with col2:
        if st.button("❌", key=i):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()

if not st.session_state.tasks:
    st.info("No tasks yet. Add one above!")
