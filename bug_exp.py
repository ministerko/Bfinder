import re
def get_bug_explanation(self, bug_type):
        explanations = {
            "Potential debug code found": "This indicates the presence \n of potential debug code (e.g., console.log), \n which may not be suitable for production environments.",
            "Potential XSS vulnerability found": "This indicates the presence of potential Cross-Site Scripting (XSS) vulnerability, \n which could be exploited by attackers to execute malicious scripts.",
            "Missing semicolon found": "This indicates a missing semicolon in the code, \n which could lead to syntax errors or unexpected behavior.",
            "Unused variable found": "This indicates the presence of an unused variable in the code, \n which may increase code complexity and decrease readability.",
            "Potential infinite loop found": "This indicates the presence of a potential infinite loop in the code, \n which may cause the program to hang or become unresponsive.",
            "Inline JavaScript found": "This indicates the presence of inline JavaScript, \n which is generally discouraged due to security and maintainability concerns.",
            "Missing alt attribute in img tag found": "This indicates the presence of an img tag without the alt attribute, \n which is essential for accessibility and SEO purposes.",
            "Broken link found": "This indicates the presence of a broken link, \n which may result in a poor user experience and negatively impact SEO.",
            "Missing doctype declaration found": "This indicates the absence of a doctype declaration, \n which may lead to rendering issues in some browsers.",
            "Deprecated HTML attribute": "This indicates the presence of a deprecated HTML attribute, \n which may not be supported in modern browsers or may lead to non-standard behavior."
        }
        return explanations.get(bug_type, "No explanation available")

def scan_js_file(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            bugs = []
                # Check for console.log
            if re.search(r'\bconsole\.log\b', content):
                bugs.append(("Potential debug code found", file_path))
        
            # Check for potential XSS vulnerabilities
            if re.search(r'\b(?:eval|document\.write|innerHTML)\b', content):
                bugs.append(("Potential XSS vulnerability found", file_path))
        
            # Check for missing semicolons
            if re.search(r'[^;];\s*(\/\/.*$|$)', content):
                bugs.append(("Missing semicolon found", file_path))
        
            # Check for unused variables
            if re.search(r'\bvar\s+(\w+)\b[^=]', content):
                bugs.append(("Unused variable found", file_path))
        
            # Check for potential infinite loops
            if re.search(r'while\s*\(.+?\)\s*{', content):
                bugs.append(("Potential infinite loop found", file_path))
        
            # Check for insecure direct object references
            if re.search(r'\bwindow\[\s*".*?"\s*\]', content):
                bugs.append(("Insecure direct object reference", file_path))
        
            # Check for insecure regular expressions
            if re.search(r'/.*/[gim]*\.\bexec\b|\.test\b|\.search\b|\.match\b', content):
                bugs.append(("Potential ReDoS vulnerability (insecure regular expression)", file_path))
        
            # Check for insecure CORS configuration
            if re.search(r'XMLHttpRequest\.withCredentials\s*=\s*true', content):
                bugs.append(("Insecure CORS configuration", file_path))
        
            # Check for insecure JSON parsing
            if re.search(r'\bJSON\.parse\s*\(', content):
                bugs.append(("Potential JSON injection vulnerability", file_path))
        
            # Check for unvalidated input from URL parameters
            if re.search(r'location\.search|\.hash', content):
                bugs.append(("Unvalidated input from URL parameters", file_path))
        
            # Check for insecure use of setTimeout()
            if re.search(r'\bsetTimeout\s*\(', content):
                bugs.append(("Potential DOS vulnerability (insecure use of setTimeout)", file_path))
        
            # Check for insecure use of setInterval()
            if re.search(r'\bsetInterval\s*\(', content):
                bugs.append(("Potential DOS vulnerability (insecure use of setInterval)", file_path))
        
            # Check for insecure use of requestAnimationFrame()
            if re.search(r'\brequestAnimationFrame\s*\(', content):
                bugs.append(("Potential DOS vulnerability (insecure use of requestAnimationFrame)", file_path))
        
            # Check for insecure use of cookies
            if re.search(r'document\.cookie\s*=', content):
                bugs.append(("Potential XSS or CSRF vulnerability (insecure use of cookies)", file_path))
        
            # Check for insecure use of local storage
            if re.search(r'localStorage\s*\[', content):
                bugs.append(("Potential XSS or data leakage (insecure use of local storage)", file_path))
        
            # Check for use of deprecated or vulnerable libraries
            if re.search(r'angular\.js|jquery\.js|prototype\.js|react\.js|vue\.js', content):
                bugs.append(("Use of deprecated or vulnerable library", file_path))
        
            # Check for insecure use of JavaScript APIs
            if re.search(r'navigator\.|screen\.|window\.\blocation\b|document\.\breferrer\b|history\.', content):
                bugs.append(("Potential privacy or security issue (insecure use of JavaScript APIs)", file_path))
        
            # Check for insecure use of insecure randomness
            if re.search(r'Math\.\brandom\b', content):
                bugs.append(("Insecure randomness (Math.random() usage)", file_path))
        
            # Check for insecure use of client-side encryption
            if re.search(r'CryptoJS\.AES|SJCL', content):
                bugs.append(("Potential data leakage (insecure client-side encryption)", file_path))
        
            # Check for insecure use of WebSockets
            if re.search(r'WebSocket\s*\(', content):
                bugs.append(("Potential DOS or XSS vulnerability (insecure use of WebSockets)", file_path))
        
            # Check for insecure use of geolocation API
            if re.search(r'navigator\.geolocation\s*\.', content):
                bugs.append(("Potential privacy issue (insecure use of geolocation API)", file_path))
        
            # Check for insecure use of FileReader API
            if re.search(r'FileReader\s*\(', content):
                bugs.append(("Potential information disclosure (insecure use of FileReader API)", file_path))
        
            # Check for insecure use of postMessage API
            if re.search(r'window\.postMessage\s*\(', content):
                bugs.append(("Potential XSS or security issue (insecure use of postMessage API)", file_path))

            return bugs
def scan_html_file(self, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        bugs = []

        if re.search(r'<script[^>]*>[^<]*<\/script>', content):
            bugs.append(("Inline JavaScript found", file_path))

        if re.search(r'<img\s+[^>]*>', content) and not re.search(r'alt\s*=\s*".*?"', content):
            bugs.append(("Missing alt attribute in img tag found", file_path))

        if re.search(r'href\s*=\s*"(.*?)"', content):
            bugs.append(("Broken link found", file_path))

        if not re.search(r'<!DOCTYPE html>', content, re.IGNORECASE):
            bugs.append(("Missing doctype declaration found", file_path))
            # Check for SQL injection bugs in form inputs
        if re.search(r'<input\s+[^>]*\btype\s*=\s*(?:"text"|"search"|"tel"|"url"|"email"|"password")[^>]*\bname\s*=\s*".*?"[^>]*>', content, re.IGNORECASE):
            bugs.append(("Potential SQL injection vulnerability in form inputs", file_path)) 

        # Check for insecure content loading (HTTP content on HTTPS page)
        if re.search(r'<(iframe|script|img|link|embed|object)\s+[^>]*\bsrc\s*=\s*"[^"]*http://', content, re.IGNORECASE):
            bugs.append(("Insecure content loading found (HTTP content on HTTPS page)", file_path))
        # Check for CSRF bugs (missing CSRF tokens)
        if re.search(r'<form[^>]*>', content) and not re.search(r'\bcsrfmiddlewaretoken\b', content):
            bugs.append(("CSRF vulnerability (missing CSRF token)", file_path))

        # Check for open redirect bugs
        if re.search(r'\bredirect_uri\s*=\s*"[^"]+', content):
            bugs.append(("Open redirect vulnerability", file_path))

        deprecated_attributes = ['align', 'bgcolor', 'border', 'cellpadding', 'cellspacing']
        for attribute in deprecated_attributes:
            if re.search(fr'\b{attribute}\b', content):
                bugs.append((f'Deprecated HTML attribute "{attribute}" found', file_path))

        return bugs
