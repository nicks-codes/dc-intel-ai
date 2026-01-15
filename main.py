from fastapi import FastAPI
from typing import List
from datetime import datetime

app = FastAPI(
    title="Data Center Expert API",
    version="1.0.0",
    description="API for real-time data center industry insights, site reports, leasing activity, and more.",
)

@app.get("/news/latest")
def get_latest_news(topic: str = None):
    news = [
        {
            "title": "Hyperscaler leases 50MW in Northern Virginia",
            "summary": "A major cloud provider signed a 50MW lease with a top operator in Ashburn, indicating ongoing demand.",
            "publishedAt": datetime.now().isoformat(),
            "url": "https://example.com/news/ashburn-lease"
        },
        {
            "title": "Power constraints slow site selection in Phoenix",
            "summary": "Developers report increasing delays due to utility challenges and transformer backlogs.",
            "publishedAt": datetime.now().isoformat(),
            "url": "https://example.com/news/phoenix-power"
        }
    ]

    if topic:
        news = [n for n in news if topic.lower() in n["summary"].lower() or topic.lower() in n["title"].lower()]
    return news

@app.get("/site-reports/{location}")
def get_site_report(location: str):
    return {
        "location": location,
        "powerAvailability": "Moderate – 6-12 month lead time for 10MW+ deployments.",
        "leasingMarket": "Strong demand, vacancy below 4%.",
        "permittingStatus": "Improving, but local zoning remains a bottleneck.",
        "recentDeals": [
            {
                "tenant": "Meta",
                "sizeMW": 36.0,
                "leaseDate": "2025-01-01"
            },
            {
                "tenant": "AWS",
                "sizeMW": 20.0,
                "leaseDate": "2025-02-15"
            }
        ]
    }

@app.get("/digest")
def get_digest():
    return {
        "summary": (
            "This week saw continued hyperscale leasing in Ashburn, "
            "despite power delays in Phoenix. Demand in Dallas remains steady. "
            "Permitting reforms in Oregon could ease developer timelines."
        ),
        "dateRange": "2026-01-08 to 2026-01-15"
    }
