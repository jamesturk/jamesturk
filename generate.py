#!/usr/bin/env python3
import feedparser

python_projects = [
    "spatula",
    "scrapelib",
    "django-honeypot",
    "scrapeghost",
    "jellyfish",
    "openstates",
    "django-markupfield",
]


def get_url(package):
    if package == "openstates":
        return "https://github.com/openstates/"
    else:
        return f"https://codeberg.org/jpt/{package}"


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
    header = """I have decided to move my work off GitHub. ([why?](https://sfconservancy.org/GiveUpGitHub/))

Repositories with lots of collaborators/users have been moved to <https://codeberg.org/jpt/> with issues/etc. intact.
    
See <https://git.unnamed.computer/jpt> for experiments & new work.

<https://jpt.sh> for other things!

| package | version | released |\n|--------------|-----------|-------------|\n"""
    return header + "\n".join(rows)


if __name__ == "__main__":
    print("## Find Me Elsewhere")
    print(format_as_markdown(get_latest_releases()))
