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
    encoded_query = urllib.parse.quote_plus(query)
    google_url = f"https://www.google.com/search?q={encoded_query}"
    st.markdown(
        f'<a href="{google_url}" target="_blank" class="button-link">Open in Google Search</a>',
        unsafe_allow_html=True
    )

# --- Helper Function for Basic Domain Validation ---
def is_valid_domain(domain):
    if not domain:
        return True
    return re.match(r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$", domain) is not None

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
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
        background-color: #008CBA;
        color: white !important;
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

# --- Tabs ---
tabs = st.tabs([
    "Cheatsheet",
    "Specific Use Cases",
    "General Query Builder",
    "Feedback"
])

# --- Tab 1: Cheatsheet ---
with tabs[0]:
    st.title("🔍 Google SEO Scout")
    st.markdown(
        """
        Welcome to **Google SEO Scout**! This app helps you build powerful Google search queries using advanced search operators.
        Effortlessly find indexing issues, analyze competitors, discover content opportunities, and more.
        """
    )
    st.header("Google Search Operators Cheatsheet")
    with st.expander("📖 View All Operators", expanded=True):
        st.markdown("""
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

# --- Tab 2: Specific Use Cases ---
with tabs[1]:
    st.header("Specific Use Cases")
    # ... (see previous message for full logic on use case selection) ...

# --- Tab 3: General Query Builder ---
with tabs[2]:
    st.header("General Query Builder")
    st.markdown("Combine various operators and keywords to create highly specific searches.")
    st.markdown("---")
    # -- Sectioned layout --
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
        st.markdown("---")
        st.subheader("AROUND(X) Operator")
        around_term1 = st.text_input("AROUND(X) - Term 1", key="gen_around_term1_final")
        around_term2 = st.text_input("AROUND(X) - Term 2", key="gen_around_term2_final")
        around_x = st.number_input("AROUND(X) - X (number of words apart)", min_value=1, value=5, key="gen_around_x_final")
        st.markdown("---")
        st.subheader("Cache Operator")
        cache_url = st.text_input("Cache URL (e.g., example.com/page)", key="gen_cache_url_final")

    generated_query_parts = []

    if site_domain and not is_valid_domain(site_domain):
        st.warning("Invalid format for 'Site' domain. Please enter a valid domain (e.g., example.com).")
        site_domain = ""
    if related_site and not is_valid_domain(related_site):
        st.warning("Invalid format for 'Related Site' domain. Please enter a valid domain (e.g., example.com).")
        related_site = ""

    # --- Assemble Query ---
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
    if around_term1 and around_term2:
        generated_query_parts.append(f"\"{around_term1}\" AROUND({around_x}) \"{around_term2}\"")
    elif around_term1 or around_term2:
        st.warning("For AROUND(X), please provide both terms.")
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

# --- Tab 4: Feedback ---
with tabs[3]:
    st.header("Feedback & Suggestions")
    st.markdown("Help us improve Google SEO Scout! Share your thoughts or suggest new operator combinations.")
    with st.form("feedback_form"):
        feedback_text = st.text_area("Your Feedback", height=100)
        submit_feedback = st.form_submit_button("Submit Feedback")
        if submit_feedback:
            if feedback_text:
                st.success("Thank you for your feedback! We appreciate your input.")
                # In a real application, you would store this feedback
            else:
                st.warning("Please enter some feedback before submitting.")

    st.markdown("---")
    st.info(
        "**Note:** Google's search results and operator behavior can change over time. "
        "This tool generates the query string; the actual search results are provided by Google."
    )
