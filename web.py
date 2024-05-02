import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)



st.title("My To-Do App")
st.subheader("This is a simple to-do app built with Streamlit")
st.write("To get started, type a task in the box below and click the 'Add' button")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input("Type a task here",
              placeholder= "Add new todo..." ,
              key="new_todo",
              on_change=add_todo)
