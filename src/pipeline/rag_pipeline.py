from typing import Any
from langchain.messages import HumanMessage


# RAG function
def rag_sys(query, retriever, llm, top_k=3):
    # Step 1: Retrieve relevant documents
    results = retriever.retrieve(query, top_k=top_k)
    
    # Step 2: Prepare context for LLM
    context = "\n\n".join([doc['content'] for doc in results]) if results else ""
    if not context:
        return "I'm sorry, I couldn't find any relevant information to answer your question."

    # Step 3: Generate response using LLM
    
    # prompt = f"""use the following context to answer the question concisely.
    # Context:
    # {context}

    # Question: {query}

    # Answer:"""

    # response = llm.invoke([prompt.format(context=context, query=query)])
    # return response.content

    prompt = """
            You are a factual AI assistant.

            Answer ONLY using the provided context.

            If the answer is not contained in the context, say:
            "I don't have enough information to answer this."
            

            Context:
            {context}

            Question:
            {query}

            Answer:
            """
    
    # response = llm.invoke([prompt.format(context=context, query=query)])

    response = llm.invoke([
    HumanMessage(content=prompt.format(
        context=context,
        query=query
        ))
    ])
    return response.content