import json

import streamlit as st

from agent import chain


def run_agent(user_input: str):
    """Invoke the existing chain with the required input mapping."""
    result = chain.invoke({"input": user_input})
    return result


def render_sources(sources):
    if not sources:
        st.info("No sources returned.")
        return
    st.subheader("Sources")
    for idx, src in enumerate(sources, start=1):
        link = getattr(src, "link", None) if hasattr(src, "link") else src.get("link")
        if link:
            st.markdown(f"{idx}. [{link}]({link})")
        else:
            st.write(f"{idx}. (missing link)")


def main():
    st.set_page_config(page_title="LLM Playground", page_icon="🤖", layout="wide")
    st.title("LLM Playground 🤖")
    st.caption("Using your existing ReAct agent and tools")

    if "history" not in st.session_state:
        st.session_state.history = []
    with st.sidebar:
        st.header("Controls")
        show_raw = st.toggle("Show raw response JSON", value=False)
        st.markdown("---")
        st.markdown(
            "Need to change model, temperature, or tools? Update these in `agent.py`."
        )

    prompt = st.text_area(
        "Enter your prompt", height=120, placeholder="Ask the agent anything..."
    )
    run_clicked = st.button("Run", type="primary")

    if run_clicked:
        if not prompt.strip():
            st.warning("Please enter a prompt.")
        else:
            with st.spinner("Thinking..."):
                try:
                    response = run_agent(prompt)
                    if hasattr(response, "model_dump"):
                        payload = response.model_dump()
                    elif hasattr(response, "dict"):
                        payload = response.dict()
                    else:
                        try:
                            payload = json.loads(
                                json.dumps(
                                    response,
                                    default=lambda o: getattr(o, "__dict__", str(o)),
                                )
                            )
                        except Exception:
                            payload = {"answer": str(response), "sources": []}

                    answer = payload.get("answer") or "(no answer provided)"
                    sources = payload.get("sources", [])

                    st.session_state.history.append(
                        {
                            "prompt": prompt,
                            "answer": answer,
                            "sources": sources,
                            "raw": payload,
                        }
                    )
                except Exception as e:
                    st.error(f"Error while running agent: {e}")

    if st.session_state.history:
        for i, item in enumerate(reversed(st.session_state.history), start=1):
            st.markdown(f"### Result {len(st.session_state.history) - i + 1}")
            st.markdown("**Prompt**:")
            st.write(item["prompt"])
            st.markdown("**Answer**:")
            st.write(item["answer"])
            render_sources(item.get("sources", []))

            if st.session_state.get("show_raw") or show_raw:
                st.markdown("**Raw**:")
                st.code(json.dumps(item.get("raw", {}), indent=2))
            st.markdown("---")

    else:
        st.info("Enter a prompt and click Run to see results.")


if __name__ == "__main__":
    main()
