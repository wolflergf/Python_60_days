import streamlit as st

from functions import add_todo, delete_todo, get_todos, update_todo_status, write_todos

st.set_page_config(page_title="To-do App", page_icon="✅", layout="wide")

st.title("📝 To-do App")

todos = get_todos()

st.sidebar.header("Add New Task")
new_todo = st.sidebar.text_input("New task", placeholder="Enter a new task...")
if st.sidebar.button("Add Task"):
    if new_todo:
        add_todo(todos, new_todo)
        st.sidebar.success("Task added successfully!")
    else:
        st.sidebar.error("Please enter a task.")

st.header("Current Tasks")

if not todos:
    st.info("No pending tasks. Add a new task!")
else:
    for index, todo in enumerate(todos):
        col1, col2, col3, col4, col5 = st.columns([0.1, 2, 1, 1, 0.5])

        with col1:
            status = st.checkbox(
                "Complete",
                key=f"todo_{index}",
                value=todo[2] in ["Completed", "Concluída"],
                label_visibility="collapsed",
            )
        with col2:
            st.write(todo[0])
        with col3:
            st.write(f"Date: {todo[1]}")
        with col4:
            status_options = ["Pending", "In progress", "Completed"]
            status_mapping = {
                "Pendente": "Pending",
                "Em andamento": "In progress",
                "Concluída": "Completed",
            }
            current_status = status_mapping.get(todo[2], todo[2])
            new_status = st.selectbox(
                "Status",
                status_options,
                index=status_options.index(current_status),
                key=f"status_{index}",
            )
        with col5:
            delete_button = st.button("🗑️", key=f"delete_{index}", help="Delete task")

        if (
            status != (todo[2] in ["Completed", "Concluída"])
            or new_status != current_status
        ):
            update_todo_status(todos, index, "Completed" if status else new_status)
            st.experimental_rerun()

        if delete_button:
            delete_todo(todos, index)
            st.experimental_rerun()

st.sidebar.markdown("---")
st.sidebar.write(f"**Total tasks: {len(todos)}**")

# Statistics
st.sidebar.header("Statistics")
status_counts = {"Pending": 0, "In progress": 0, "Completed": 0}
for todo in todos:
    mapped_status = status_mapping.get(todo[2], todo[2])
    status_counts[mapped_status] += 1

for status, count in status_counts.items():
    st.sidebar.write(f"{status}: {count}")

# Styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    .stTextInput>div>div>input {
        background-color: white;
        color: black;
    }
    .stSelectbox>div>div>select {
        background-color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
