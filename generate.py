#!/usr/bin/env python3
import feedparser

python_projects = [
    "spatula",
    "scrapelib",
    "django-honeypot",
    "rrl",
    "scrapeghost",
    "jellyfish",
    "django-markupfield",
    "openstates",
    "gcr-cli",
]


def get_url(package):
    if package == "openstates":
        return "https://github.com/openstates/"
    else:
        return f"https://github.com/jamesturk/{package}"


def get_release(name):
    pypi_feed = f"https://pypi.org/rss/project/{name}/releases.xml"
    latest = feedparser.parse(pypi_feed)["entries"][0]
    pub = latest["published_parsed"]
    return {
        "package": name,
        "version": latest["title"],
        "published": f"{pub.tm_year}-{pub.tm_mon:02d}-{pub.tm_mday:02d}",
        "url": get_url(name),
    }


def get_latest_releases():
    projects = sorted(
        [get_release(proj) for proj in python_projects],
        key=lambda p: p["published"],
        reverse=True,
    )
    return projects


def format_as_markdown(releases):
    rows = [
        "| [{package}]({url}) | {version} | {published} |".format(**proj)
        for proj in releases
    ]
    header = """| package | version | released |\n|--------------|-----------|-------------|\n"""
    return header + "\n".join(rows)


if __name__ == "__main__":
    print("## Latest Releases")
    print(format_as_markdown(get_latest_releases()))
