import streamlit as st
import pymunk

def main():
    st.title("B'Eng'd")
    st.write("Build machines and see them in action!")
    
    # Initialize the physics space
    space = pymunk.Space()
    space.gravity = (0, -1000)

    # Simple simulation loop (placeholder for now)
    st.write("Physics simulation will go here.")

if __name__ == "__main__":
    main()
