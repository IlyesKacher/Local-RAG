

def simplify_nq_example(nq_example):
    """
    Simplify the NQ example by extracting text and removing HTML and byte offsets.
    """
    # Extract the document text from tokens
    document_text = " ".join([token["token"] for token in nq_example["document_tokens"]])

    # Extract the question text
    question_text = nq_example["question_text"]

    # Extract the answer text from the long answer span
    long_answer_span = nq_example["annotations"][0]["long_answer"]
    long_answer_text = " ".join(
        token["token"] for token in nq_example["document_tokens"]
        if long_answer_span["start_byte"] <= token["start_byte"] <= long_answer_span["end_byte"]
    )

    # Extract the short answer text from the short answer spans
    short_answers_text = [" ".join(
        token["token"] for token in nq_example["document_tokens"]
        if sa["start_byte"] <= token["start_byte"] <= sa["end_byte"]
    ) for sa in nq_example["annotations"][0]["short_answers"]]

    # Create a simplified example
    simplified_example = {
        "example_id": nq_example["example_id"],
        "document_url": nq_example["document_url"],
        "question_text": question_text,
        "document_text": document_text,
        "long_answer_text": long_answer_text,
        "short_answers_text": short_answers_text
    }

    return simplified_example