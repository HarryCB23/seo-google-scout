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
tab_cheatsheet, tab_use_cases, tab_general_builder, tab_feedback = st.tabs([
    "📖 Cheatsheet", "🎯 Specific Use Cases", "🛠️ General Query Builder", "💬 Feedback"
])

### TAB 1: Cheatsheet
with tab_cheatsheet:
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

### TAB 2: Specific Use Cases (ALL USE CASES INCLUDED)
with tab_use_cases:
    st.header("Specific Use Cases")
    st.markdown("Choose a use case to quickly generate a targeted Google search query.")

    use_case_options = [
        "🕸️ Find Possible Indexing Issues",
        "⚔️ Find and Analyze Your Competitors",
        "✍️ Find Guest Post Opportunities",
        "📚 Find Resource Page Opportunities",
        "📄 Find Specific File Types on a Site",
        "🔗 Find Opportunities to Add Internal Links",
        "🏆 Find “Best” Listicles that Don’t Mention Your Brand",
        "⭐ Find Websites that Have Reviewed Competitors",
        "💬 Find Relevant Quora and Reddit Questions to Answer",
        "⚡ Find How Fast Your Competitors are Publishing New Content",
        "🔒 Find Non-Secure Pages",
        "📝 Find Plagiarized Content",
        "🧑‍💻 Find Prolific Guest Bloggers",
        "📈 Find Competitor's Top Pages for a Keyword",
        "🔢 Find Content in a Numeric Range",
        "📄 Find Credible Sources for Articles",
        "📊 Find Infographic Submission Opportunities",
        "👤 Find Social Profiles for Outreach",
        "🗣️ Join Social Conversations on Forums",
        "🌐 Find Mentions on Specific Platforms",
        "🗓️ Find Outdated Content",
        "💰 Find Sponsored Post Opportunities",
        "🔍 Find Competitor's Content by Topic"
    ]
    selected_case = st.selectbox("Choose a use case", use_case_options)

    # For each use case, show relevant input, build query, and allow opening in Google.
    # For brevity, here are the first two; add all rest in similar style.

    if selected_case == "🕸️ Find Possible Indexing Issues":
        st.subheader("Find Possible Indexing Issues")
        domain = st.text_input("Your Website Domain (e.g., yoursite.com)", key="indexing_domain")
        if st.button("Generate Query", key="indexing_btn"):
            if domain and is_valid_domain(domain):
                query = f"site:{domain}"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter a valid domain.")

    elif selected_case == "⚔️ Find and Analyze Your Competitors":
        st.subheader("Find and Analyze Your Competitors")
        competitor_domain = st.text_input("Competitor Domain (e.g., competitor.com)", key="comp_domain")
        keyword = st.text_input("Keyword (optional)", key="comp_keyword")
        if st.button("Generate Query", key="comp_btn"):
            query = ""
            if competitor_domain and is_valid_domain(competitor_domain):
                query += f"related:{competitor_domain} "
            if keyword:
                query += f"{keyword}"
            query = query.strip()
            if query:
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter domain or keyword.")

    elif selected_case == "✍️ Find Guest Post Opportunities":
        st.subheader("Find Guest Post Opportunities")
        niche = st.text_input("Your Niche (e.g., SEO)", key="guest_niche")
        phrases = st.multiselect("Guest Post Phrases",
            ["\"write for us\"", "\"guest post\"", "\"contribute\"", "\"submit a post\"", "\"guest blogging guidelines\""],
            default=["\"write for us\""], key="guest_phrases")
        if st.button("Generate Query", key="guest_btn"):
            if niche and phrases:
                phrase_query = " | ".join(phrases)
                query = f"{niche} ({phrase_query})"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter niche and select phrases.")

    elif selected_case == "📚 Find Resource Page Opportunities":
        st.subheader("Find Resource Page Opportunities")
        topic = st.text_input("Topic/Keyword (e.g., SEO tools)", key="resource_topic")
        if st.button("Generate Query", key="resource_btn"):
            if topic:
                query = f"{topic} (intitle:resources | inurl:resource | intitle:links | inurl:links | intitle:directory)"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter a topic.")

    elif selected_case == "📄 Find Specific File Types on a Site":
        st.subheader("Find Specific File Types on a Site")
        file_site = st.text_input("Site Domain (optional, e.g., yoursite.com)", key="file_site")
        file_keywords = st.text_input("Keywords (optional)", key="file_keywords")
        file_types = st.multiselect(
            "File Types", ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "csv", "xml", "txt", "zip", "sql", "env", "bak"],
            default=["pdf"], key="file_types")
        if st.button("Generate Query", key="file_btn"):
            query = ""
            if file_site and is_valid_domain(file_site):
                query += f"site:{file_site} "
            if file_keywords:
                query += f"{file_keywords} "
            if file_types:
                query += "(" + " | ".join([f"filetype:{ft}" for ft in file_types]) + ")"
            query = query.strip()
            if query:
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please fill at least one field.")

    elif selected_case == "🔗 Find Opportunities to Add Internal Links":
        st.subheader("Find Opportunities to Add Internal Links")
        site = st.text_input("Your Site/Blog Domain", key="internal_link_site")
        keyword = st.text_input("Target Keyword", key="internal_link_keyword")
        if st.button("Generate Query", key="internal_link_btn"):
            if site and is_valid_domain(site) and keyword:
                query = f"site:{site} \"{keyword}\""
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter domain and keyword.")

    elif selected_case == "🏆 Find “Best” Listicles that Don’t Mention Your Brand":
        st.subheader("Find “Best” Listicles that Don’t Mention Your Brand")
        brand = st.text_input("Your Brand Name", key="listicle_brand")
        topic = st.text_input("Listicle Topic", key="listicle_topic")
        if st.button("Generate Query", key="listicle_btn"):
            if brand and topic:
                query = f"intitle:best \"{topic}\" -\"{brand}\""
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter brand and topic.")

    elif selected_case == "⭐ Find Websites that Have Reviewed Competitors":
        st.subheader("Find Websites that Have Reviewed Competitors")
        competitors = st.text_area("Competitor Brands (one per line)", key="review_competitors")
        if st.button("Generate Query", key="review_btn"):
            brands = [b.strip() for b in competitors.split('\n') if b.strip()]
            if brands:
                query = f"allintitle:review ({' OR '.join([f'\"{b}\"' for b in brands])})"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter at least one competitor.")

    elif selected_case == "💬 Find Relevant Quora and Reddit Questions to Answer":
        st.subheader("Find Relevant Quora and Reddit Questions to Answer")
        topics = st.text_input("Topics (comma separated)", key="qa_topics")
        if st.button("Generate Query", key="qa_btn"):
            topic_query = " | ".join([t.strip() for t in topics.split(',') if t.strip()])
            if topic_query:
                query = f"(site:quora.com OR site:reddit.com) inurl:({topic_query})"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter topics.")

    elif selected_case == "⚡ Find How Fast Your Competitors are Publishing New Content":
        st.subheader("Find How Fast Your Competitors are Publishing New Content")
        domain = st.text_input("Competitor Domain", key="comp_speed_domain")
        after = st.date_input("Published After Date", value=None, key="comp_speed_after")
        before = st.date_input("Published Before Date", value=None, key="comp_speed_before")
        if st.button("Generate Query", key="comp_speed_btn"):
            query = ""
            if domain and is_valid_domain(domain):
                query += f"site:{domain} "
            if after:
                query += f"after:{after.strftime('%Y-%m-%d')} "
            if before:
                query += f"before:{before.strftime('%Y-%m-%d')}"
            query = query.strip()
            if query:
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please fill at least one field.")

    elif selected_case == "🔒 Find Non-Secure Pages":
        st.subheader("Find Non-Secure Pages")
        domain = st.text_input("Your Website Domain", key="non_secure_domain")
        if st.button("Generate Query", key="non_secure_btn"):
            if domain and is_valid_domain(domain):
                query = f"site:{domain} -inurl:https"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter domain.")

    elif selected_case == "📝 Find Plagiarized Content":
        st.subheader("Find Plagiarized Content")
        text = st.text_area("Exact Text Snippet", key="plagiarism_text")
        if st.button("Generate Query", key="plagiarism_btn"):
            if text:
                query = f"allintext:\"{text}\""
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter a text snippet.")

    elif selected_case == "🧑‍💻 Find Prolific Guest Bloggers":
        st.subheader("Find Prolific Guest Bloggers")
        niche = st.text_input("Niche/Keywords", key="blogger_niche")
        author = st.text_input("Specific Author Name (optional)", key="blogger_author")
        if st.button("Generate Query", key="blogger_btn"):
            query = ""
            if niche:
                query += niche + " "
            if author:
                formatted = author.lower().replace(" ", "-")
                query += f"inurl:author/{formatted}"
            else:
                query += "inurl:author/"
            query = query.strip()
            if query:
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter a niche or author.")

    elif selected_case == "📈 Find Competitor's Top Pages for a Keyword":
        st.subheader("Find Competitor's Top Pages for a Keyword")
        domain = st.text_input("Competitor Domain", key="top_pages_domain")
        keyword = st.text_input("Keyword/Topic", key="top_pages_keyword")
        if st.button("Generate Query", key="top_pages_btn"):
            if domain and is_valid_domain(domain) and keyword:
                query = f"site:{domain} inurl:\"{keyword}\""
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter domain and keyword.")

    elif selected_case == "🔢 Find Content in a Numeric Range":
        st.subheader("Find Content in a Numeric Range")
        keywords = st.text_input("Keywords", key="numeric_keywords")
        min_value = st.number_input("Min Value", min_value=0, value=10, key="min_value")
        max_value = st.number_input("Max Value", min_value=0, value=100, key="max_value")
        currency_symbol = st.text_input("Currency Symbol (optional)", max_chars=1, key="currency_symbol")
        if st.button("Generate Query", key="numeric_btn"):
            if min_value < max_value:
                range_query = f"{currency_symbol}{min_value}..{currency_symbol}{max_value}"
                query = f"{keywords} {range_query}".strip()
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Min value must be less than max value.")

    elif selected_case == "📄 Find Credible Sources for Articles":
        st.subheader("Find Credible Sources for Articles")
        keywords = st.text_input("Keywords for Research", key="source_keywords")
        file_types = st.multiselect("File Types", ["pdf", "ppt", "pptx", "doc", "docx"], default=["pdf"], key="source_file_types")
        if st.button("Generate Query", key="source_btn"):
            if keywords and file_types:
                filetype_query = " | ".join([f"filetype:{ft}" for ft in file_types])
                query = f"{keywords} ({filetype_query})"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please fill both fields.")

    elif selected_case == "📊 Find Infographic Submission Opportunities":
        st.subheader("Find Infographic Submission Opportunities")
        niche = st.text_input("Niche/Keywords", key="infographic_niche")
        phrases = st.multiselect("Submission Phrases", ["\"submit infographic\"", "\"infographic submission\"", "\"post infographic\""], default=["\"submit infographic\""], key="infographic_phrases")
        if st.button("Generate Query", key="infographic_btn"):
            if niche and phrases:
                phrase_query = " | ".join([f"intitle:{p} OR inurl:{p.replace('\"','').replace(' ','-')}" for p in phrases])
                query = f"{niche} ({phrase_query})"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please fill both fields.")

    elif selected_case == "👤 Find Social Profiles for Outreach":
        st.subheader("Find Social Profiles for Outreach")
        name = st.text_input("Brand or Person Name", key="social_name")
        platforms = st.multiselect("Platforms", ["linkedin.com", "twitter.com", "facebook.com", "instagram.com", "youtube.com"], default=["linkedin.com", "twitter.com"], key="social_platforms")
        if st.button("Generate Query", key="social_btn"):
            if name and platforms:
                site_query = " OR ".join([f"site:{p}" for p in platforms])
                query = f"\"{name}\" ({site_query})"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please fill both fields.")

    elif selected_case == "🗣️ Join Social Conversations on Forums":
        st.subheader("Join Social Conversations on Forums")
        topic = st.text_input("Topic Keywords", key="conversation_topic")
        forum_sites = st.multiselect("Forum Sites", ["reddit.com", "quora.com"], default=["reddit.com", "quora.com"], key="forum_sites")
        custom_forum = st.text_input("Custom Forum Domain (optional)", key="custom_forum")
        if st.button("Generate Query", key="conversation_btn"):
            all_sites = forum_sites
            if custom_forum and is_valid_domain(custom_forum):
                all_sites.append(custom_forum)
            site_query = " OR ".join([f"site:{s}" for s in all_sites])
            if topic and all_sites:
                query = f"({site_query}) \"{topic}\" (intext:question | intext:discussion | intitle:forum)"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter a topic and at least one forum.")

    elif selected_case == "🌐 Find Mentions on Specific Platforms":
        st.subheader("Find Mentions on Specific Platforms")
        keywords = st.text_input("Brand/Topic Keywords", key="mention_keywords")
        platforms = st.multiselect("Platforms", ["docs.google.com", "drive.google.com", "slideshare.net", "medium.com", "notion.so"], default=["docs.google.com"], key="mention_platforms")
        custom_platform = st.text_input("Custom Platform Domain (optional)", key="custom_platform")
        if st.button("Generate Query", key="mention_btn"):
            all_sites = platforms
            if custom_platform and is_valid_domain(custom_platform):
                all_sites.append(custom_platform)
            site_query = " OR ".join([f"site:{s}" for s in all_sites])
            if keywords and all_sites:
                query = f"\"{keywords}\" ({site_query})"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please fill both fields.")

    elif selected_case == "🗓️ Find Outdated Content":
        st.subheader("Find Outdated Content")
        domain = st.text_input("Website Domain", key="outdated_domain")
        year_before = st.number_input("Published Before Year", min_value=1990, max_value=datetime.now().year, value=datetime.now().year-2, key="outdated_year")
        keywords = st.text_input("Keywords (optional)", key="outdated_keywords")
        if st.button("Generate Query", key="outdated_btn"):
            if domain and is_valid_domain(domain):
                query = f"site:{domain} \"{keywords}\" before:{year_before}-01-01" if keywords else f"site:{domain} before:{year_before}-01-01"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter a valid domain.")

    elif selected_case == "💰 Find Sponsored Post Opportunities":
        st.subheader("Find Sponsored Post Opportunities")
        niche = st.text_input("Niche/Keywords", key="sponsored_niche")
        phrases = st.multiselect("Sponsored Post Phrases", ["\"sponsored post\"", "\"this post was sponsored by\"", "\"advertorial\"", "\"paid post\""], default=["\"sponsored post\""], key="sponsored_phrases")
        if st.button("Generate Query", key="sponsored_btn"):
            if niche and phrases:
                phrase_query = " | ".join([f"intext:{p} OR intitle:{p}" for p in phrases])
                query = f"{niche} ({phrase_query})"
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please fill both fields.")

    elif selected_case == "🔍 Find Competitor's Content by Topic":
        st.subheader("Find Competitor's Content by Topic")
        domain = st.text_input("Competitor Domain", key="comp_topic_domain")
        keywords = st.text_input("Topic Keywords", key="comp_topic_keywords")
        if st.button("Generate Query", key="comp_topic_btn"):
            if domain and is_valid_domain(domain) and keywords:
                query = f"site:{domain} \"{keywords}\""
                st.code(query)
                open_google_search(query)
            else:
                st.warning("Please enter domain and keywords.")

### TAB 3: General Query Builder
with tab_general_builder:
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
    if keywords: parts.append(keywords)
    if site_domain: parts.append(f"site:{site_domain}")
    if inurl: parts.append(f"inurl:{inurl}")
    if intitle: parts.append(f'intitle:{intitle}')
    if filetype: parts.append(f"filetype:{filetype}")
    if exact_match: parts.append(f"\"{exact_match}\"")
    if exclude: parts.append(f"-{exclude}")
    if or_terms: parts.append(f"({or_terms})")
    if before: parts.append(f"before:{before}")
    if after: parts.append(f"after:{after}")
    if term1 and term2: parts.append(f"\"{term1}\" AROUND({around_x}) \"{term2}\"")
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

### TAB 4: Feedback
with tab_feedback:
    st.header("Feedback & Suggestions")
    st.markdown("Help us improve Google SEO Scout! Share your thoughts or suggest new operator combinations.")
    with st.form("feedback_form"):
        feedback_text = st.text_area("Your Feedback", height=100)
        submit_feedback = st.form_submit_button("Submit Feedback")
        if submit_feedback:
            if feedback_text:
                st.success("Thank you for your feedback! We appreciate your input.")
            else:
                st.warning("Please enter some feedback before submitting.")

    st.markdown("---")
    st.info(
        "**Note:** Google's search results and operator behavior can change over time. "
        "This tool generates the query string; the actual search results are provided by Google."
    )
