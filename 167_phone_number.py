phone_re = re.compile(r'''
\(? # optionally match begin parenthesis
(?P<area>\d{3}) # match/name group for area code
\)? # optionally match end parenthesis
[\s.-]? # optionally match space, period, or hyphen
(?P<prefix>\d{3}) # match/name group for prefix
[\s.-]? # optionally match space, period, or hyphen
(?P<suffix>\d{4}) # match/name group for suffix
''', re.VERBOSE)
phone_re.sub(r'\g<area>-\g<prefix>-\g<suffix>', '(213)555-1212')
phone_re.sub(r'\g<area>-\g<prefix>-\g<suffix>', '213.555.1212')
