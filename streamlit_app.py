import streamlit as st
import urllib.parse
import re
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
    st.markdown("""
        Welcome to **Google SEO Scout**! This app helps you build powerful Google search queries using advanced search operators.
        Effortlessly find indexing issues, analyze competitors, discover content opportunities, and more.
        """)
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
    st.markdown("""
        Choose a use case to quickly generate a targeted Google search query.
    """)

    use_case_options = [
        "Find Guest Post Opportunities",
        "Check Site Indexing",
        "Competitor Content Analysis",
        "Discover PDF Resources",
        "Custom"
    ]
    selected_case = st.selectbox("Choose a use case", use_case_options)

    # Default values
    keywords, site, inurl, intitle, filetype = "", "", "", "", ""

    if selected_case == "Find Guest Post Opportunities":
        st.markdown("**Find Guest Post Opportunities**")
        site = st.text_input("Domain to target (optional, e.g. example.com)", key="gp_site")
        keywords = st.text_input("Keywords", value="guest post", key="gp_keywords")
        inurl = "guest-post"
        intitle = "write for us"
    elif selected_case == "Check Site Indexing":
        st.markdown("**Check Site Indexing**")
        site = st.text_input("Domain to check index status (e.g. example.com)", key="idx_site")
        keywords = ""
    elif selected_case == "Competitor Content Analysis":
        st.markdown("**Competitor Content Analysis**")
        site = st.text_input("Competitor domain (e.g. example.com)", key="comp_site")
        keywords = st.text_input("Competitor keywords", key="comp_keywords")
    elif selected_case == "Discover PDF Resources":
        st.markdown("**Discover PDF Resources**")
        keywords = st.text_input("Topic for PDFs", key="pdf_keywords")
        filetype = "pdf"
        site = st.text_input("Domain to target (optional, e.g. example.com)", key="pdf_site")
    elif selected_case == "Custom":
        st.info("Use the General Query Builder tab for custom combinations.")

    query_parts = []
    if keywords: query_parts.append(keywords)
    if site: query_parts.append(f"site:{site}")
    if inurl: query_parts.append(f"inurl:{inurl}")
    if intitle: query_parts.append(f'intitle:"{intitle}"')
    if filetype: query_parts.append(f"filetype:{filetype}")

    specific_query = " ".join(query_parts).strip()
    st.markdown("---")
    st.subheader("Generated Query")
    st.code(specific_query if specific_query else "Your query will appear here.")

    if st.button("Open Specific Query in Google"):
        if specific_query:
            open_google_search(specific_query)
        else:
            st.warning("Please build a query first!")

# --- Tab 3: General Query Builder ---
with tabs[2]:
    st.header("General Query Builder")
    st.markdown("Build your custom Google search by combining operators below.")

    # --- Core Search Terms ---
    st.subheader("Core Search Terms")
    keywords = st.text_input("Main Keyword", key="core_keywords")

    # --- Domain & URL Filters ---
    st.subheader("Domain & URL Filters")
    site_domain = st.text_input("site: (Domain filter)", key="domain_site")
    inurl = st.text_input("inurl: (URL keyword)", key="domain_inurl")
    intitle = st.text_input("intitle: (Title keyword)", key="domain_intitle")
    filetype = st.text_input("filetype: (Filetype filter)", key="domain_filetype")

    # --- Inclusion & Exclusion ---
    st.subheader("Inclusion & Exclusion")
    exact_match = st.text_input("Exact Match (use quotes)", key="inc_exact")
    exclude = st.text_input("Exclude terms (prefix with '-')", key="inc_exclude")
    or_terms = st.text_input("OR terms (separate with OR)", key="inc_or")

    # --- Date & Proximity ---
    st.subheader("Date & Proximity")
    before = st.text_input("before: (YYYY-MM-DD)", key="date_before")
    after = st.text_input("after: (YYYY-MM-DD)", key="date_after")
    term1 = st.text_input("AROUND(X) term 1", key="prox_term1")
    term2 = st.text_input("AROUND(X) term 2", key="prox_term2")
    around_x = st.number_input("AROUND(X) value", min_value=1, value=5, key="prox_x")

    # --- Niche Operators (Advanced) ---
    with st.expander("Niche Operators (Advanced)"):
        related = st.text_input("related: (Find similar sites)", key="niche_related")
        cache = st.text_input("cache: (View cached version)", key="niche_cache")

    # --- Build query string ---
    parts = []
    # Core
    if keywords: parts.append(keywords)
    # Domain & URL
    if site_domain: parts.append(f"site:{site_domain}")
    if inurl: parts.append(f"inurl:{inurl}")
    if intitle: parts.append(f'intitle:{intitle}')
    if filetype: parts.append(f"filetype:{filetype}")
    # Inclusion & Exclusion
    if exact_match: parts.append(f"\"{exact_match}\"")
    if exclude: parts.append(f"-{exclude}")
    if or_terms: parts.append(f"({or_terms})")
    # Date & Proximity
    if before: parts.append(f"before:{before}")
    if after: parts.append(f"after:{after}")
    if term1 and term2: parts.append(f"\"{term1}\" AROUND({around_x}) \"{term2}\"")
    # Niche Operators
    if related: parts.append(f"related:{related}")
    if cache: parts.append(f"cache:{cache}")

    query_str = " ".join(parts)
    st.markdown("---")
    st.subheader("Generated Query")
    st.code(query_str if query_str else "Your query will appear here as you add terms.")

    if st.button("Open General Query in Google"):
        if query_str:
            open_google_search(query_str)
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
