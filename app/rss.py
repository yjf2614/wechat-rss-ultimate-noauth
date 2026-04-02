from fastapi.responses import Response

def generate_rss(articles, biz):
    items = ""
    for t,l,c,p in articles:
        items += f"""
        <item>
            <title>{t}</title>
            <link>{l}</link>
            <description><![CDATA[{c}]]></description>
        </item>
        """

    return Response(f"""
    <rss><channel><title>{biz}</title>{items}</channel></rss>
    """, media_type="application/xml")