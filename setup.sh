mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"btech15106.22@bitmesra.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml