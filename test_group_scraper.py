"""
Test script: scrape posts from a public Facebook group.
Group: https://www.facebook.com/groups/1466088316786306/
"""
import json
import traceback
from facebook_scraper import get_posts, enable_logging

# Uncomment to see verbose HTTP logs:
# enable_logging()

GROUP_ID = 1466088316786306
PAGES = 1  # Limit to 1 page for a quick test


def main():
    print(f"Attempting to scrape group {GROUP_ID} ...\n")
    try:
        posts = list(get_posts(group=GROUP_ID, pages=PAGES))
        if not posts:
            print("No posts returned. The group may require login or be private.")
            return

        print(f"Success! Got {len(posts)} post(s).\n")
        for i, post in enumerate(posts, 1):
            print(f"--- Post {i} ---")
            print(f"  post_id   : {post.get('post_id')}")
            print(f"  time      : {post.get('time')}")
            print(f"  username  : {post.get('username')}")
            print(f"  text      : {str(post.get('text', ''))[:200]}")
            print(f"  likes     : {post.get('likes')}")
            print(f"  comments  : {post.get('comments')}")
            print(f"  post_url  : {post.get('post_url')}")
            print()

    except Exception as e:
        print(f"Error while scraping: {type(e).__name__}: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
