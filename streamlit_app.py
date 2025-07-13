import streamlit as st
import urllib.parse
from datetime import datetime
import re

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Google SEO Scout",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Helper Function to Open Google Search ---
def open_google_search(query):
    """Opens a new browser tab with the generated Google search query."""
    encoded_query = urllib.parse.quote_plus(query)
    google_url = f"https://www.google.com/search?q={encoded_query}"
    st.markdown(f'<a href="{google_url}" target="_blank" class="button-link">Open in Google Search</a>', unsafe_allow_html=True)

# --- Helper Function for Basic Domain Validation ---
def is_valid_domain(domain):
    """Checks if the input string is a plausible domain."""
    if not domain:
        return True # Allow empty, as it's optional in some cases
    # Simple regex for domain: at least one word character, followed by a dot, then another word character
    # This is not exhaustive but catches common errors like just "http://"
    # Updated regex to be a bit more robust for common domain patterns
    return re.match(r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$", domain) is not None

# --- Custom CSS for Styling (Optional but Recommended for Buttons) ---
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .button-link {
        display: inline-block;
        background-color: #008CBA; /* Blue */
        color: white !important; /* Override Streamlit's default link color */
        padding: 10px 24px;
        border-radius: 8px;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        transition: background-color 0.3s ease;
        margin-top: 10px;
    }
    .button-link:hover {
        background-color: #007B9E;
        color: white !important;
    }
    .stExpander {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #333;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 8px;
    }
    .stDateInput>div>div>input {
        border-radius: 8px;
        padding: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- App Title and Introduction ---
st.title("🔍 Google SEO Scout")
st.markdown(
    """
    Welcome to **Google SEO Scout**! This app helps you build powerful Google search queries using advanced search operators.
    Effortlessly find indexing issues, analyze competitors, discover content opportunities, and more.
    """
)

# --- Google Search Operators Cheatsheet (Moved to top) ---
st.header("Google Search Operators Cheatsheet")
with st.expander("📖 View All Operators", expanded=False):
    st.markdown("""
    This table provides a quick reference for common Google search operators and their functions.

    | Operator | What it does | Example |
    |---|---|---|
    | `" "` | Forces exact-match searches. | `"nikola tesla"` |
    | `OR` | Searches for results related to X or Y, not necessarily both. | `tesla OR edison` |
    | `|` | Functions identically to "OR." | `tesla | edison` |
    | `()` | Groups operators to control the order of execution. | `(tesla OR edison) alternating current` |
    | `-` | Excludes terms from search results. | `tesla -motors` |
    | `*` | Acts as a wildcard for matching any word or phrase. | `tesla "rock * roll"` |
    | `..` | Searches within a range of numbers. | `logitech keyboard $50..$60` |
    | `$` | Searches for specific prices. | `tesla deposit $1000` |
    | `€` | Searches for prices in euros. | `€9.99 lunch deals` |
    | `in` | Converts units. | `250 kph in mph` |
    | `define:` | Searches for the definition of a word or phrase. | `define:telescope` |
    | `filetype:` | Searches for specific types of files. | `"tesla announcements" filetype:pdf` |
    | `ext:` | Same as filetype, searching for specific file extensions. | `azure ext:pdf` |
    | `site:` | Searches within a specific website. | `site:goodwill.org` |
    | `intitle:` | Searches only within page titles. | `intitle:"tesla vs edison"` |
    | `allintitle:` | Searches for every term following "allintitle" within page titles. | `allintitle: tesla vs edison` |
    | `inurl:` | Looks for words or phrases within a URL. | `tesla announcements inurl:2024` |
    | `allinurl:` | Searches the URL for every term following "allinurl." | `allinurl: amazon field-keywords nikon` |
    | `intext:` | Searches for words or phrases within the body text of a document. | `intext:"orbi vs eero vs google wifi"` |
    | `allintext:` | Searches the body text for every term following "allintext." | `allintext: orbi eero google wifi` |
    | `AROUND(X)` | Finds terms within X words of each other in a text. | `tesla AROUND(3) edison` |
    | `weather:` | Searches for the weather in a specified location. | `weather:New Jersey` |
    | `stocks:` | Searches for stock information using a ticker symbol. | `stocks:nvidia` |
    | `map:` | Forces Google to show map results for a location. | `map:Manhattan` |
    | `movie:` | Searches for information about a specific movie. | `movie:Oppenheimer` |
    | `source:` | Searches for news from a specific source. | `deepseek source:cnn` |
    | `before:` | Searches for results before a specific date. | `Microsoft before:2010-05-08` |
    | `after:` | Searches for results after a specific date. | `Microsoft after:2010-05-08` |
    | `cache:` | Displays Google's cached version of a web page. | `cache:example.com` |
    | `info:` | Presents information about a web page. | `info:example.com` |
    | `related:` | Finds sites related to a specified domain. | `related:nytimes.com` |
    """)

st.markdown("---")

# --- Specific Use Cases (Now a Dropdown) ---
st.header("Specific Use Cases")
use_case_options = {
    "Select a Use Case": None, # Default option
    "🕸️ 1. Find Possible Indexing Issues": "indexing_issues",
    "⚔️ 2. Find and Analyze Your Competitors": "analyze_competitors",
    "✍️ 3. Find Guest Post Opportunities": "guest_post_opportunities",
    "📚 4. Find Resource Page Opportunities": "resource_page_opportunities",
    "📄 5. Find Specific File Types on a Site": "specific_file_types",
    "🔗 6. Find Opportunities to Add Internal Links": "internal_linking",
    "🏆 7. Find “Best” Listicles that Don’t Mention Your Brand": "best_listicles",
    "⭐ 8. Find Websites that Have Reviewed Competitors": "competitor_reviews",
    "💬 9. Find Relevant Quora and Reddit Questions to Answer": "qa_sites",
    "⚡ 10. Find How Fast Your Competitors are Publishing New Content": "competitor_content_speed",
    "🔒 11. Find Non-Secure Pages": "non_secure_pages",
    "📝 12. Find Plagiarized Content": "plagiarized_content",
    "🧑‍💻 13. Find Prolific Guest Bloggers": "prolific_guest_bloggers",
    "📈 14. Find Competitor's Top Pages for a Keyword": "competitor_top_pages",
    "🔢 15. Find Content in a Numeric Range": "numeric_range",
    "📄 16. Find Credible Sources for Articles": "credible_sources",
    "📊 17. Find Infographic Submission Opportunities": "infographic_submission", # New
    "👤 18. Find Social Profiles for Outreach": "social_profiles", # New
    "🗣️ 19. Join Social Conversations on Forums": "social_conversations" # New
}

selected_use_case_display = st.selectbox(
    "Choose a specific SEO/Research task:",
    options=list(use_case_options.keys()),
    key="use_case_selector"
)
selected_use_case_id = use_case_options[selected_use_case_display]

# Conditional rendering for each use case
if selected_use_case_id == "indexing_issues":
    st.subheader("🕸️ Find Possible Indexing Issues")
    st.markdown("Check how many pages of your site Google has indexed.")
    indexing_domain = st.text_input("Your Website Domain (e.g., yoursite.com)", key="indexing_domain")
    
    if st.button("Generate Query for Indexing", key="indexing_button"):
        if indexing_domain:
            if not is_valid_domain(indexing_domain):
                st.warning("Invalid format for domain. Please enter a valid domain (e.g., yoursite.com).")
            else:
                query = f"site:{indexing_domain}"
                st.code(query)
                open_google_search(query)
        else:
            st.warning("Please enter a domain.")

elif selected_use_case_id == "analyze_competitors":
    st.subheader("⚔️ Find and Analyze Your Competitors")
    st.markdown("Discover similar sites or find competitors targeting specific keywords.")
    comp_domain = st.text_input("Competitor Domain (for 'related:' operator, e.g., competitor.com)", key="comp_domain")
    comp_keywords = st.text_input("Keywords for InTitle/InText (e.g., 'digital marketing')", key="comp_keywords")
    comp_intitle_checkbox = st.checkbox("Use intitle: for keywords", key="comp_intitle_checkbox")

    if st.button("Generate Query for Competitors", key="competitors_button"):
        if comp_domain and not is_valid_domain(comp_domain):
            st.warning("Invalid format for 'Competitor Domain'. Please enter a valid domain (e.g., competitor.com).")
        else:
            query_parts = []
            if comp_domain:
                query_parts.append(f"related:{comp_domain}")
            if comp_keywords:
                if comp_intitle_checkbox:
                    query_parts.append(f"intitle:\"{comp_keywords}\"")
                else:
                    query_parts.append(comp_keywords)
            
            query = " ".join(query_parts).strip()
            if query:
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter at least a competitor domain or keywords.")

elif selected_use_case_id == "guest_post_opportunities":
    st.subheader("✍️ 3. Find Guest Post Opportunities")
    st.markdown("Find websites in your niche that accept guest contributions.")
    guest_niche = st.text_input("Your Niche/Keywords (e.g., 'content marketing')", key="guest_niche")
    guest_phrases = st.multiselect(
        "Common Guest Post Phrases",
        ["\"write for us\"", "\"contribute\"", "\"guest post\"", "\"submit a post\"", "\"guest blogging guidelines\""],
        default=["\"write for us\""],
        key="guest_phrases"
    )
    if st.button("Generate Query for Guest Posts", key="guest_post_button"):
        if guest_niche and guest_phrases:
            phrase_query = " | ".join(guest_phrases)
            query = f"{guest_niche} ({phrase_query})"
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter a niche and select at least one phrase.")

elif selected_use_case_id == "resource_page_opportunities":
    st.subheader("📚 4. Find Resource Page Opportunities")
    st.markdown("Identify pages that list external resources, potentially for backlink opportunities.")
    resource_topic = st.text_input("Your Topic (e.g., 'SEO tools')", key="resource_topic")
    if st.button("Generate Query for Resource Pages", key="resource_page_button"):
        if resource_topic:
            query = f"{resource_topic} (intitle:resources | inurl:resource | intitle:links | inurl:links | intitle:directory)"
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter a topic.")

elif selected_use_case_id == "specific_file_types":
    st.subheader("📄 5. Find Specific File Types on a Site")
    st.markdown("Locate specific file types (e.g., PDFs, presentations) on a given site or broadly.")
    file_search_scope = st.radio(
        "Search Scope",
        ("On a specific site", "Broadly across the web"),
        key="file_search_scope"
    )
    file_site_optional = ""
    if file_search_scope == "On a specific site":
        file_site_optional = st.text_input("Site Domain (e.g., yoursite.com)", key="file_site_optional")
        if file_site_optional and not is_valid_domain(file_site_optional):
            st.warning("Invalid format for 'Site Domain'. Please enter a valid domain (e.g., yoursite.com).")
            file_site_optional = "" # Clear invalid input
    
    file_types_to_find = st.multiselect(
        "File Types to Find",
        ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "csv", "xml", "txt", "zip", "sql", "env", "bak"],
        default=["pdf"],
        key="file_types_to_find"
    )
    file_keywords = st.text_input("Keywords (optional, e.g., 'report')", key="file_keywords")

    if st.button("Generate Query for File Types", key="file_type_button"):
        if not file_types_to_find:
            st.warning("Please select at least one file type.")
        elif file_search_scope == "On a specific site" and not file_site_optional:
            st.warning("Please enter a site domain for specific site search.")
        else:
            query_parts = []
            if file_site_optional:
                query_parts.append(f"site:{file_site_optional}")
            if file_keywords:
                query_parts.append(file_keywords)
            
            filetype_query = " | ".join([f"filetype:{ft}" for ft in file_types_to_find])
            query_parts.append(f"({filetype_query})")
            
            query = " ".join(query_parts).strip()
            st.code(query)
            open_google_search(query)

elif selected_use_case_id == "internal_linking":
    st.subheader("🔗 6. Find Opportunities to Add Internal Links")
    st.markdown("Discover pages on your site that could link to a target page or topic.")
    internal_link_site = st.text_input("Your Blog/Site URL (e.g., yoursite.com/blog)", key="internal_link_site")
    internal_link_keyword = st.text_input("Target Keyword/Phrase (e.g., 'content strategy')", key="internal_link_keyword")
    if st.button("Generate Query for Internal Links", key="internal_links_button"):
        if internal_link_site and not is_valid_domain(internal_link_site): # Basic check for URL-like input
            st.warning("Invalid format for 'Your Blog/Site URL'. Please enter a valid domain or URL (e.g., yoursite.com/blog).")
        elif internal_link_site and internal_link_keyword:
            query = f"site:{internal_link_site} \"{internal_link_keyword}\""
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter your site URL and a target keyword.")

elif selected_use_case_id == "best_listicles":
    st.subheader("🏆 7. Find “Best” Listicles that Don’t Mention Your Brand")
    st.markdown("Identify 'best of' lists that could be opportunities for your brand to be included.")
    your_brand = st.text_input("Your Brand Name (e.g., 'MyAwesomeTool')", key="your_brand")
    listicle_topic = st.text_input("Topic Keyword (e.g., 'project management software')", key="listicle_topic")
    if st.button("Generate Query for Listicles", key="listicles_button"):
        if your_brand and listicle_topic:
            query = f"intitle:best \"{listicle_topic}\" -\"{your_brand}\""
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter your brand name and a topic.")

elif selected_use_case_id == "competitor_reviews":
    st.subheader("⭐ 8. Find Websites that Have Reviewed Competitors")
    st.markdown("Find sites that have reviewed your competitors, indicating potential review opportunities for your brand.")
    competitor_brands_input = st.text_area("Competitor Brand Names (one per line)", key="competitor_brands_input")
    if st.button("Generate Query for Competitor Reviews", key="competitor_reviews_button"):
        competitor_brands = [brand.strip() for brand in competitor_brands_input.split('\n') if brand.strip()]
        if competitor_brands:
            brands_query = " OR ".join([f"\"{brand}\"" for brand in competitor_brands])
            query = f"allintitle:review ({brands_query})"
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter at least one competitor brand name.")

elif selected_use_case_id == "qa_sites":
    st.subheader("💬 9. Find Relevant Quora and Reddit Questions to Answer")
    st.markdown("Discover questions on popular forums related to your topics for content ideas or direct engagement.")
    qa_topics_input = st.text_input("Topic Keywords (comma-separated, e.g., 'AI, machine learning')", key="qa_topics_input")
    if st.button("Generate Query for Q&A Sites", key="qa_sites_button"):
        qa_topics = [topic.strip() for topic in qa_topics_input.split(',') if topic.strip()]
        if qa_topics:
            topic_query = " | ".join(qa_topics)
            query = f"(site:quora.com OR site:reddit.com) inurl:({topic_query})"
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter topic keywords.")

elif selected_use_case_id == "competitor_content_speed":
    st.subheader("⚡ 10. Find How Fast Your Competitors are Publishing New Content")
    st.markdown("Monitor competitor content publication frequency within a specific timeframe.")
    comp_content_domain = st.text_input("Competitor Domain (e.g., competitorblog.com)", key="comp_content_domain")
    content_after_date = st.date_input("Published After Date", value=None, key="content_after_date")
    content_before_date = st.date_input("Published Before Date", value=None, key="content_before_date")

    if st.button("Generate Query for Competitor Content Speed", key="comp_content_speed_button"):
        if comp_content_domain and not is_valid_domain(comp_content_domain):
            st.warning("Invalid format for 'Competitor Domain'. Please enter a valid domain (e.g., competitorblog.com).")
        else:
            query_parts = [f"site:{comp_content_domain}"]
            if content_after_date:
                query_parts.append(f"after:{content_after_date.strftime('%Y-%m-%d')}")
            if content_before_date:
                query_parts.append(f"before:{content_before_date.strftime('%Y-%m-%d')}")
            
            query = " ".join(query_parts).strip()
            if query_parts:
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter a competitor domain and at least one date.")

elif selected_use_case_id == "non_secure_pages":
    st.subheader("🔒 11. Find Non-Secure Pages")
    st.markdown("Identify pages on your site that are not using HTTPS.")
    non_secure_domain = st.text_input("Your Website Domain (e.g., yoursite.com)", key="non_secure_domain")
    if st.button("Generate Query for Non-Secure Pages", key="non_secure_button"):
        if non_secure_domain:
            if not is_valid_domain(non_secure_domain):
                st.warning("Invalid format for domain. Please enter a valid domain (e.g., yoursite.com).")
            else:
                query = f"site:{non_secure_domain} -inurl:https"
                st.code(query)
                open_google_search(query)
        else:
            st.warning("Please enter a domain.")

elif selected_use_case_id == "plagiarized_content":
    st.subheader("📝 12. Find Plagiarized Content")
    st.markdown("Search for exact matches of your content across the web to detect plagiarism.")
    plagiarism_text = st.text_area("Exact text snippet to search for (e.g., a sentence or paragraph from your content)", key="plagiarism_text")
    if st.button("Generate Query for Plagiarized Content", key="plagiarism_button"):
        if plagiarism_text:
            query = f"allintext:\"{plagiarism_text}\""
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter a text snippet.")

elif selected_use_case_id == "prolific_guest_bloggers":
    st.subheader("🧑‍💻 13. Find Prolific Guest Bloggers")
    st.markdown("Discover authors who frequently publish guest posts in your niche.")
    blogger_niche = st.text_input("Niche/Keywords (e.g., 'SEO')", key="blogger_niche")
    specific_author = st.text_input("Specific Author Name (optional, e.g., 'neil patel')", key="specific_author")
    if st.button("Generate Query for Guest Bloggers", key="guest_blogger_button"):
        query_parts = []
        if blogger_niche:
            query_parts.append(blogger_niche)
        
        if specific_author:
            # Format author name for URL (e.g., neil-patel)
            formatted_author = specific_author.lower().replace(" ", "-")
            query_parts.append(f"inurl:author/{formatted_author}")
        else:
            query_parts.append("inurl:author/") # Search for any author URL pattern

        query = " ".join(query_parts).strip()
        if query:
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter a niche/keywords.")

elif selected_use_case_id == "competitor_top_pages":
    st.subheader("📈 14. Find Competitor's Top Pages for a Keyword")
    st.markdown("Identify popular pages on a competitor's site related to a specific keyword or topic.")
    comp_top_pages_domain = st.text_input("Competitor Domain (e.g., moz.com)", key="comp_top_pages_domain")
    comp_top_pages_keyword = st.text_input("Keyword/Topic in URL (e.g., 'link building')", key="comp_top_pages_keyword")
    if st.button("Generate Query for Competitor Top Pages", key="comp_top_pages_button"):
        if comp_top_pages_domain and not is_valid_domain(comp_top_pages_domain):
            st.warning("Invalid format for 'Competitor Domain'. Please enter a valid domain (e.g., moz.com).")
        elif comp_top_pages_domain and comp_top_pages_keyword:
            query = f"site:{comp_top_pages_domain} inurl:\"{comp_top_pages_keyword}\""
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter both competitor domain and a keyword/topic.")

elif selected_use_case_id == "numeric_range":
    st.subheader("🔢 15. Find Content in a Numeric Range")
    st.markdown("Search for content containing numbers within a specified range (e.g., prices, years).")
    numeric_keywords = st.text_input("Keywords (e.g., 'best laptops')", key="numeric_keywords")
    min_value = st.number_input("Minimum Value", min_value=0, value=10, key="min_value")
    max_value = st.number_input("Maximum Value", min_value=0, value=100, key="max_value")
    currency_symbol = st.text_input("Optional Currency Symbol (e.g., $, £, €)", key="currency_symbol", max_chars=1)

    if st.button("Generate Query for Numeric Range", key="numeric_range_button"):
        if min_value >= max_value:
            st.warning("Minimum value must be less than maximum value.")
        else:
            range_query = f"{currency_symbol}{min_value}..{currency_symbol}{max_value}"
            query = f"{numeric_keywords} {range_query}".strip()
            st.code(query)
            open_google_search(query)

elif selected_use_case_id == "credible_sources":
    st.subheader("� 16. Find Credible Sources for Articles")
    st.markdown("Locate academic papers, reports, or presentations in specific file formats for research.")
    source_keywords = st.text_input("Keywords for Research (e.g., 'LLM training data')", key="source_keywords")
    source_file_types = st.multiselect(
        "Preferred File Types",
        ["pdf", "ppt", "pptx", "doc", "docx"],
        default=["pdf"],
        key="source_file_types"
    )
    if st.button("Generate Query for Credible Sources", key="credible_sources_button"):
        if source_keywords and source_file_types:
            filetype_query = " | ".join([f"filetype:{ft}" for ft in source_file_types])
            query = f"{source_keywords} ({filetype_query})"
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter keywords and select at least one file type.")

# --- NEW USE CASE: Infographic Submission Opportunities ---
elif selected_use_case_id == "infographic_submission":
    st.subheader("📊 17. Find Infographic Submission Opportunities")
    st.markdown("Discover websites that accept infographic submissions in your niche.")
    infographic_niche = st.text_input("Your Niche/Keywords (e.g., 'data visualization')", key="infographic_niche")
    infographic_phrases = st.multiselect(
        "Submission Phrases",
        ["\"submit infographic\"", "\"infographic submission\"", "\"post infographic\""],
        default=["\"submit infographic\""],
        key="infographic_phrases"
    )
    if st.button("Generate Query for Infographic Submission", key="infographic_submission_button"):
        if infographic_niche and infographic_phrases:
            phrase_query = " | ".join([f"intitle:\"{p}\" OR inurl:{p.replace('\"','').replace(' ','-')}" for p in infographic_phrases])
            query = f"{infographic_niche} ({phrase_query})"
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter a niche and select at least one phrase.")

# --- NEW USE CASE: Find Social Profiles for Outreach ---
elif selected_use_case_id == "social_profiles":
    st.subheader("👤 18. Find Social Profiles for Outreach")
    st.markdown("Locate social media profiles for a brand or person for outreach purposes.")
    profile_name = st.text_input("Brand or Person Name (e.g., 'Elon Musk' or 'Tesla')", key="profile_name")
    social_platforms = st.multiselect(
        "Select Social Media Platforms",
        ["linkedin.com", "twitter.com", "facebook.com", "instagram.com", "youtube.com"],
        default=["linkedin.com", "twitter.com"],
        key="social_platforms"
    )
    if st.button("Generate Query for Social Profiles", key="social_profiles_button"):
        if profile_name and social_platforms:
            platform_query = " OR ".join([f"site:{p}" for p in social_platforms])
            query = f"\"{profile_name}\" ({platform_query})"
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter a name and select at least one platform.")

# --- NEW USE CASE: Join Social Conversations on Forums ---
elif selected_use_case_id == "social_conversations":
    st.subheader("🗣️ 19. Join Social Conversations on Forums")
    st.markdown("Find relevant discussions on forums like Reddit and Quora related to your topic.")
    conversation_topic = st.text_input("Topic Keywords (e.g., 'AI ethics')", key="conversation_topic")
    forum_sites = st.multiselect(
        "Select Forum Sites (add custom domains too)",
        ["reddit.com", "quora.com"],
        default=["reddit.com", "quora.com"],
        key="forum_sites"
    )
    custom_forum_site = st.text_input("Add Custom Forum Domain (e.g., 'stackexchange.com')", key="custom_forum_site")

    if st.button("Generate Query for Social Conversations", key="social_conversations_button"):
        if conversation_topic and (forum_sites or custom_forum_site):
            all_sites = list(forum_sites)
            if custom_forum_site and is_valid_domain(custom_forum_site):
                all_sites.append(custom_forum_site)
            elif custom_forum_site and not is_valid_domain(custom_forum_site):
                st.warning("Invalid format for 'Custom Forum Domain'. Please enter a valid domain.")
                all_sites = [] # Prevent invalid domain from being used

            if all_sites:
                site_query = " OR ".join([f"site:{s}" for s in all_sites])
                query = f"({site_query}) \"{conversation_topic}\" (intext:question | intext:discussion | intitle:forum)"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter a topic and select/add at least one forum site.")
        else:
            st.warning("Please enter a topic and select/add at least one forum site.")


st.markdown("---")

# --- General Query Builder (Moved to bottom) ---
st.header("General Query Builder")
with st.expander("🛠️ Build Your Custom Query", expanded=True):
    st.markdown("Combine various operators and keywords to create highly specific searches.")

    col1, col2 = st.columns(2)
    with col1:
        keywords = st.text_input("General Keywords (e.g., 'SEO tips')", key="gen_keywords_final")
        site_domain = st.text_input("Site (e.g., example.com)", key="gen_site_final")
        intitle_phrase = st.text_input("InTitle (exact phrase, e.g., 'write for us')", key="gen_intitle_final")
        inurl_phrase = st.text_input("InURL (exact phrase, e.g., 'guest-post')", key="gen_inurl_final")
        filetype_ext = st.text_input("Filetype (e.g., pdf, doc, xls)", key="gen_filetype_final")

    with col2:
        exact_match_phrase = st.text_input("Exact Match Phrase (\"...\")", key="gen_exact_match_final")
        exclude_term = st.text_input("Exclude Term (-term)", key="gen_exclude_final")
        or_terms = st.text_input("OR Terms (term1 | term2)", help="Use '|' for OR, e.g., 'marketing | SEO'", key="gen_or_final")
        before_date = st.date_input("Before Date (YYYY-MM-DD)", value=None, key="gen_before_final")
        after_date = st.date_input("After Date (YYYY-MM-DD)", value=None, key="gen_after_final")
        related_site = st.text_input("Related Site (e.g., example.com)", key="gen_related_final")
        
        # AROUND(X) operator
        st.markdown("---")
        st.subheader("AROUND(X) Operator")
        around_term1 = st.text_input("AROUND(X) - Term 1", key="gen_around_term1_final")
        around_term2 = st.text_input("AROUND(X) - Term 2", key="gen_around_term2_final")
        around_x = st.number_input("AROUND(X) - X (number of words apart)", min_value=1, value=5, key="gen_around_x_final")

        # cache: operator
        st.markdown("---")
        st.subheader("Cache Operator")
        cache_url = st.text_input("Cache URL (e.g., example.com/page)", key="gen_cache_url_final")


    generated_query_parts = []
    
    # Input validation for domains
    if site_domain and not is_valid_domain(site_domain):
        st.warning("Invalid format for 'Site' domain. Please enter a valid domain (e.g., example.com).")
        site_domain = "" # Clear invalid input
    if related_site and not is_valid_domain(related_site):
        st.warning("Invalid format for 'Related Site' domain. Please enter a valid domain (e.g., example.com).")
        related_site = "" # Clear invalid input

    if keywords:
        generated_query_parts.append(keywords)
    if site_domain:
        generated_query_parts.append(f"site:{site_domain}")
    if intitle_phrase:
        generated_query_parts.append(f"intitle:\"{intitle_phrase}\"")
    if inurl_phrase:
        generated_query_parts.append(f"inurl:\"{inurl_phrase}\"")
    if filetype_ext:
        generated_query_parts.append(f"filetype:{filetype_ext}")
    if exact_match_phrase:
        generated_query_parts.append(f"\"{exact_match_phrase}\"")
    if exclude_term:
        generated_query_parts.append(f"-{exclude_term}")
    if or_terms:
        # Handle OR terms, ensuring they are grouped if multiple
        or_list = [term.strip() for term in or_terms.split('|') if term.strip()]
        if len(or_list) > 1:
            generated_query_parts.append(f"({' | '.join(or_list)})")
        elif or_list:
            generated_query_parts.append(or_list[0])
    if before_date:
        generated_query_parts.append(f"before:{before_date.strftime('%Y-%m-%d')}")
    if after_date:
        generated_query_parts.append(f"after:{after_date.strftime('%Y-%m-%d')}")
    if related_site:
        generated_query_parts.append(f"related:{related_site}")
    
    # Add AROUND(X) to query
    if around_term1 and around_term2:
        generated_query_parts.append(f"\"{around_term1}\" AROUND({around_x}) \"{around_term2}\"")
    elif around_term1 or around_term2:
        st.warning("For AROUND(X), please provide both terms.")

    # Add cache: to query
    if cache_url:
        generated_query_parts.append(f"cache:{cache_url}")


    general_query = " ".join(generated_query_parts).strip()

    st.markdown("---")
    st.subheader("Generated Query:")
    st.code(general_query if general_query else "Your query will appear here as you add operators.")

    if st.button("Open General Query in Google", key="open_general_query_final"):
        if general_query:
            open_google_search(general_query)
        else:
            st.warning("Please build a query first!")

st.markdown("---")

# --- User Feedback Section ---
st.header("Feedback & Suggestions")
st.markdown("Help us improve Google SEO Scout! Share your thoughts or suggest new operator combinations.")
with st.form("feedback_form"):
    feedback_text = st.text_area("Your Feedback", height=100)
    submit_feedback = st.form_submit_button("Submit Feedback")
    if submit_feedback:
        if feedback_text:
            st.success("Thank you for your feedback! We appreciate your input.")
            # In a real application, you would store this feedback (e.g., to a database, email, or file)
        else:
            st.warning("Please enter some feedback before submitting.")

st.markdown("---")
st.info(
    "**Note:** Google's search results and operator behavior can change over time. "
    "This tool generates the query string; the actual search results are provided by Google."
)
