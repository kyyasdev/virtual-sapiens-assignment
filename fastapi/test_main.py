from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_summaries_api_returns_10_words():
    # My example
    text = "Lorem ipsum dolor sit amet consectetur adipiscing elit cras congue massa quam in venenatis sapien ultricies eu Nullam et dui"
    
    response = client.post(
        "/summaries",
        json={"text": text}
    )
    
    assert response.status_code == 200  # check 1
    
    data = response.json()
    assert "summary" in data    # check 2
    
    # Split to words & count them
    summary_words = data["summary"].split()
    assert len(summary_words) == 10     # check 3
    
    # Verify it's the first 10 words
    expected_words = text.split()[:10]
    assert summary_words == expected_words  # check 4


def test_summaries_endpoint_returns_timestamp():
    # example
    text = "This is a test sentence."
    
    response = client.post(
        "/summaries",
        json={"text": text}
    )
    
    assert response.status_code == 200  # check 1
    
    data = response.json()
    assert "timestamp" in data, "Response should contain a 'timestamp' field"  # check 2