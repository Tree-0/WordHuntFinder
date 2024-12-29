// In the future if you host the backend change the API_URL to the hosted URL.
const API_URL = 'http://127.0.0.1:5000';

// Call the API to fetch solutions
export const fetchWordHuntSolutions = async (letters: string): Promise<string[]> => {
  try {
    // Right now requires Flask backend to be running
    const response = await fetch(`${API_URL}/wordhunt`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ letters }),
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    return await response.json();
  } catch (err: unknown) {
    return err instanceof Error ? [err.message] : ['Error: An unknown error occurred'];
  }
}

export const fetchAnagramsSolutions = async (letters: string): Promise<string[]> => {
  try {
    // 
    const response = await fetch(`${API_URL}/anagrams`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ letters }),
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    return await response.json();
  } catch (err: unknown) {
    return err instanceof Error ? [err.message] : ['Error: An unknown error occurred'];
  }
}
