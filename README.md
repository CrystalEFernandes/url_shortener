# Django URL Shortener

A simple URL shortening service built with Django that provides functionalities to shorten URLs, redirect to the original URLs, manage expiration, track analytics, and allow updating or deleting short URLs.

---

## Features

1. **URL Shortening**:
   - Accepts a long URL and optionally a custom alias to generate a short URL.
   - Automatically assigns an alias if a custom one is not provided.

2. **Redirection**:
   - Redirects users from the short URL to the original URL as long as it has not expired.

3. **Time-to-Live (TTL)**:
   - URLs are valid for a configurable duration (default: 120 seconds).
   - Expired URLs are no longer accessible.

4. **Analytics**:
   - Tracks the number of times a short URL was accessed and the timestamps of each access.

5. **Update Functionality**:
   - Update the alias or extend the TTL of an existing short URL.

6. **Deletion**:
   - Delete a specific short URL and its associated data.

---

## Screenshots

1. **Shorten URL (POST Request)**:
   ![shortenURL](https://github.com/user-attachments/assets/c3581902-8433-4508-a1af-6a06bef6a29d)

2. **Redirect to Long URL (GET Request):**
   ![getURLalias](https://github.com/user-attachments/assets/8f503204-ffa6-44e2-a105-e4fdef4eab16)

3. **Get Analytics (GET Request):**
   ![analyticsAlias](https://github.com/user-attachments/assets/562e467c-9060-4056-b8f7-392ca3201e7c)
   ![analyticsAlias2](https://github.com/user-attachments/assets/ac627414-94f4-4418-bf30-e7b7f2edafb9)

4. **Update URL (PUT Request):**
  ![updateAlias](https://github.com/user-attachments/assets/a1b40860-80ff-4405-a6b4-3a777bcf62d9)
  ![updatedAnalytics](https://github.com/user-attachments/assets/64b7d1a5-f485-4535-b117-7db534db9abd)

5. **Delete URL (DELETE Request):**
  ![delete](https://github.com/user-attachments/assets/86d29cd3-0c21-4f50-9ba6-397e934ec91b)

