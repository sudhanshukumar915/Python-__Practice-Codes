# mic_test.py - A simple tool to check if the microphone is working

import speech_recognition as sr


def test_microphone():
    """Checks if the microphone can hear and recognize speech."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("--- Microphone Test ---")
        print("Calibrating for 2 seconds... Please be quiet.")
        r.adjust_for_ambient_noise(source, duration=2)
        print("Calibration complete.")

        print("\nPlease say something in HINDI (जैसे 'नमस्ते दुनिया')...")

        try:
            # Listen for 5 seconds
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Got it! Now recognizing...")

            # Try to recognize the speech using Google Speech Recognition
            text = r.recognize_google(audio, language='hi-in')
            print("\nSUCCESS! The microphone heard:")
            print(f">>> {text} <<<")

        except sr.WaitTimeoutError:
            print("\nERROR: No speech was detected within 5 seconds.")
        except sr.UnknownValueError:
            print("\nERROR: Google Speech Recognition could not understand the audio.")
            print("This could be due to low mic volume, too much background noise, or unclear speech.")
        except sr.RequestError as e:
            print(f"\nERROR: Could not request results from Google service; {e}")
            print("Please check your internet connection.")
        except Exception as e:
            print(f"\nAN UNKNOWN ERROR OCCURRED: {e}")


if __name__ == "__main__":
    test_microphone()