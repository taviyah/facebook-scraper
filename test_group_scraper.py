"""
Cautious scraper for a public Facebook group.
Group: https://www.facebook.com/groups/1466088316786306/

Safety guidelines:
  - Keep PAGES low (1-2 per run). Don't scrape hundreds of pages in one go.
  - Keep DELAY_BETWEEN_POSTS at least 3-5 seconds.
  - Don't run this more than once or twice a day.
  - Use cookies from your browser (see README for how to export them).
  - Required cookies: c_user and xs (both must be present).
"""

import time
import traceback
from facebook_scraper import get_posts
from facebook_scraper import exceptions

GROUP_ID = 1466088316786306

# --- Safety settings ---
COOKIES_FILE = "cookies.txt"  # Export from browser; must contain c_user and xs
PAGES = 1                     # Keep low. Each page = ~8-10 posts.
DELAY_BETWEEN_POSTS = 5       # Seconds to wait between processing each post.
                              # The scraper fetches lazily, so this paces requests.


def main():
    print(f"Scraping group {GROUP_ID} (pages={PAGES}, delay={DELAY_BETWEEN_POSTS}s) ...\n")

    try:
        post_iter = get_posts(
            group=GROUP_ID,
            cookies=COOKIES_FILE,
            pages=PAGES,
        )

        count = 0
        for post in post_iter:
            count += 1
            print(f"--- Post {count} ---")
            print(f"  post_id  : {post.get('post_id')}")
            print(f"  time     : {post.get('time')}")
            print(f"  username : {post.get('username')}")
            print(f"  text     : {str(post.get('text', ''))[:200]}")
            print(f"  likes    : {post.get('likes')}")
            print(f"  comments : {post.get('comments')}")
            print(f"  post_url : {post.get('post_url')}")
            print()

            time.sleep(DELAY_BETWEEN_POSTS)

        if count == 0:
            print("No posts returned. The group may be private or the cookies may be invalid.")
        else:
            print(f"Done. Scraped {count} post(s).")

    except exceptions.InvalidCookies as e:
        print(f"Cookie error: {e}")
        print("Re-export your cookies from the browser and update cookies.txt.")
    except exceptions.LoginRequired as e:
        print(f"Login required: {e}")
        print("Make sure cookies.txt exists and contains valid c_user and xs cookies.")
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
