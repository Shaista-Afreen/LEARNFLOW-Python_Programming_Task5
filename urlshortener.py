#Install necessary library
#pip install pyshorteners
import pyshorteners

# Dictionary to store mappings 
url_mappings = {}

def create_short_url(original_url):
    url_shortener = pyshorteners.Shortener()
    shortened_url = url_shortener.tinyurl.short(original_url)
    url_mappings[shortened_url] = original_url  # Store mapping in memory
    return shortened_url

def redirect_to_original(short_url):
    if short_url in url_mappings:
        original_url = url_mappings[short_url]
        return original_url  # Return the original URL for redirection
    else:
        return None  # Return None if short URL not found


if __name__ == "__main__":

    print("Welcome to the URL Shortening Service!")
    print("-------------------------------------")

    link_to_shorten = input("Please enter a long URL to shorten: ")
    shortened_link = create_short_url(link_to_shorten)
    print("The shortened URL is: " + shortened_link)
    
    # Asking user if they want to redirect
    choice = input("Do you want to redirect to the original URL? (yes/no): ").lower()
    
    if choice == "yes":
        short_url_to_redirect = input("Enter the shortened URL to redirect to original: ")
        original_url = redirect_to_original(short_url_to_redirect)
        if original_url:
            print(f"Redirecting to: {original_url}")
        else:
            print("Short URL not found. Please check the entered URL.")
    else:
        print("No redirection requested. Exiting program.")
