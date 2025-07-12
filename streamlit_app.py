import streamlit as st
import urllib.parse
from datetime import datetime

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
    Select a module below or use the general query builder to get started.
    """
)

# --- General Query Builder ---
st.header("General Query Builder")
with st.expander("Build Your Custom Query", expanded=True):
    st.markdown("Combine various operators and keywords to create highly specific searches.")

    col1, col2 = st.columns(2)
    with col1:
        keywords = st.text_input("General Keywords (e.g., 'SEO tips')", key="gen_keywords")
        site_domain = st.text_input("Site (e.g., example.com)", key="gen_site")
        intitle_phrase = st.text_input("InTitle (exact phrase, e.g., 'write for us')", key="gen_intitle")
        inurl_phrase = st.text_input("InURL (exact phrase, e.g., 'guest-post')", key="gen_inurl")
        filetype_ext = st.text_input("Filetype (e.g., pdf, doc, xls)", key="gen_filetype")

    with col2:
        exact_match_phrase = st.text_input("Exact Match Phrase (\"...\")", key="gen_exact_match")
        exclude_term = st.text_input("Exclude Term (-term)", key="gen_exclude")
        or_terms = st.text_input("OR Terms (term1 | term2)", help="Use '|' for OR, e.g., 'marketing | SEO'", key="gen_or")
        before_date = st.date_input("Before Date (YYYY-MM-DD)", value=None, key="gen_before")
        after_date = st.date_input("After Date (YYYY-MM-DD)", value=None, key="gen_after")
        related_site = st.text_input("Related Site (e.g., example.com)", key="gen_related")

    generated_query_parts = []
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

    general_query = " ".join(generated_query_parts).strip()

    st.markdown("---")
    st.subheader("Generated Query:")
    st.code(general_query if general_query else "Your query will appear here as you add operators.")

    if st.button("Open General Query in Google", key="open_general_query"):
        if general_query:
            open_google_search(general_query)
        else:
            st.warning("Please build a query first!")

st.markdown("---")
st.header("Specific Use Cases")

# --- 1. Find Possible Indexing Issues ---
with st.expander("1. Find Possible Indexing Issues"):
    st.markdown("Check how many pages of your site Google has indexed.")
    indexing_domain = st.text_input("Your Website Domain (e.g., yoursite.com)", key="indexing_domain")
    if st.button("Generate Query for Indexing", key="indexing_button"):
        if indexing_domain:
            query = f"site:{indexing_domain}"
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter a domain.")

# --- 2. Find and Analyze Your Competitors ---
with st.expander("2. Find and Analyze Your Competitors"):
    st.markdown("Discover similar sites or find competitors targeting specific keywords.")
    comp_domain = st.text_input("Competitor Domain (for 'related:' operator, e.g., competitor.com)", key="comp_domain")
    comp_keywords = st.text_input("Keywords for InTitle/InText (e.g., 'digital marketing')", key="comp_keywords")
    comp_intitle_checkbox = st.checkbox("Use intitle: for keywords", key="comp_intitle_checkbox")

    if st.button("Generate Query for Competitors", key="competitors_button"):
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

# --- 3. Find Guest Post Opportunities ---
with st.expander("3. Find Guest Post Opportunities"):
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

# --- 4. Find Resource Page Opportunities ---
with st.expander("4. Find Resource Page Opportunities"):
    st.markdown("Identify pages that list external resources, potentially for backlink opportunities.")
    resource_topic = st.text_input("Your Topic (e.g., 'SEO tools')", key="resource_topic")
    if st.button("Generate Query for Resource Pages", key="resource_page_button"):
        if resource_topic:
            query = f"{resource_topic} (intitle:resources | inurl:resource | intitle:links | inurl:links | intitle:directory)"
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter a topic.")

# --- 5. Find Files You Don’t Want in Google’s Index ---
with st.expander("5. Find Files You Don’t Want in Google’s Index"):
    st.markdown("Locate unintended file types (e.g., sensitive documents) indexed on your site.")
    file_site = st.text_input("Your Site Domain (e.g., yoursite.com)", key="file_site")
    file_types = st.multiselect(
        "File Types to Find",
        ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "csv", "xml", "txt", "zip", "sql", "env", "bak"],
        default=["pdf", "doc", "xls"],
        key="file_types"
    )
    if st.button("Generate Query for Unwanted Files", key="unwanted_files_button"):
        if file_site and file_types:
            filetype_query = " | ".join([f"filetype:{ft}" for ft in file_types])
            query = f"site:{file_site} ({filetype_query})"
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter a domain and select at least one file type.")

# --- 6. Find Opportunities to Add Internal Links ---
with st.expander("6. Find Opportunities to Add Internal Links"):
    st.markdown("Discover pages on your site that could link to a target page or topic.")
    internal_link_site = st.text_input("Your Blog/Site URL (e.g., yoursite.com/blog)", key="internal_link_site")
    internal_link_keyword = st.text_input("Target Keyword/Phrase (e.g., 'content strategy')", key="internal_link_keyword")
    if st.button("Generate Query for Internal Links", key="internal_links_button"):
        if internal_link_site and internal_link_keyword:
            query = f"site:{internal_link_site} \"{internal_link_keyword}\""
            st.code(query)
            open_google_search(query)
        else:
            st.warning("Please enter your site URL and a target keyword.")

# --- 7. Find “Best” Listicles that Don’t Mention Your Brand ---
with st.expander("7. Find “Best” Listicles that Don’t Mention Your Brand"):
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

# --- 8. Find Websites that Have Reviewed Competitors ---
with st.expander("8. Find Websites that Have Reviewed Competitors"):
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

# --- 9. Find Relevant Quora and Reddit Questions to Answer ---
with st.expander("9. Find Relevant Quora and Reddit Questions to Answer"):
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

# --- 10. Find How Fast Your Competitors are Publishing New Content ---
with st.expander("10. Find How Fast Your Competitors are Publishing New Content"):
    st.markdown("Monitor competitor content publication frequency within a specific timeframe.")
    comp_content_domain = st.text_input("Competitor Domain (e.g., competitorblog.com)", key="comp_content_domain")
    content_after_date = st.date_input("Published After Date", value=None, key="content_after_date")
    content_before_date = st.date_input("Published Before Date", value=None, key="content_before_date")

    if st.button("Generate Query for Competitor Content Speed", key="comp_content_speed_button"):
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

st.markdown("---")
st.info(
    "**Note:** Google's search results and operator behavior can change over time. "
    "This tool generates the query string; the actual search results are provided by Google."
)
