import re
from dash import hooks
from typing import List


def setup_console_filter_plugin(keywords: List[str]):
    """Setup the console filter plugin

    Args:
        keywords (List[str]): List of keywords to filter, messages containing any of these keywords in the console of the browser will be filtered
    """

    @hooks.index()
    def add_console_filter(app_index: str):
        # Extract the first line of the footer part
        match = re.findall("[ ]+<footer>", app_index)

        if match:
            # Add the console filter script
            app_index = app_index.replace(
                match[0],
                match[0]
                + """
<script type="application/javascript">
    // Replace the original console.error function
    const originalConsoleError = console.error;

    console.error = function (...args) {
        const filterKeywords = __KEYWORDS__;
        // Check if any of the arguments contain any of the filter keywords
        const shouldFilter = args.some(arg => typeof arg === 'string' && filterKeywords.some(keyword => arg.includes(keyword)));
        // If not filtered, call the original console.error function
        if (!shouldFilter) {
            originalConsoleError.apply(console, args);
        }
    };
</script>""".replace("__KEYWORDS__", str(keywords)),
            )

        return app_index
