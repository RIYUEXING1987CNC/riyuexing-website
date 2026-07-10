# -*- coding: utf-8 -*-
"""Generates products/index.html (hub) and products/{slug}.html (15 SEO detail pages)
for RI YUE XING Precision Industrial website, from the product knowledge base."""
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "products")
os.makedirs(OUT_DIR, exist_ok=True)

PRODUCTS = [
    {
        "slug": "cnc-turning-parts", "name": "CNC Turning Parts",
        "tagline": "General custom CNC turned parts manufactured according to customer drawings.",
        "materials": ["Stainless Steel", "Aluminum", "Brass", "Copper", "Titanium"],
        "applications": ["Industrial machinery", "Automation equipment", "Pneumatic components", "Hydraulic systems", "Automotive components", "Motorcycle components", "Medical devices", "Electronics", "Semiconductor equipment"],
        "industries": ["Industrial Equipment", "Automotive Industry", "Electronics Industry", "Pneumatic & Hydraulic"],
        "benefits": ["High precision", "Stable quality", "Flexible production", "OEM manufacturing", "Long-term supply"],
        "seo": ["CNC Turning Parts", "Custom CNC Turned Parts", "Precision Machined Components", "OEM CNC Parts", "Custom Metal Components"],
        "related": ["pins-dowels", "shafts-rods", "stainless-steel-parts"],
    },
    {
        "slug": "pins-dowels", "name": "Pins & Dowels",
        "tagline": "Precision locating pins and dowels for positioning and assembly.",
        "materials": ["Stainless Steel", "Brass", "Titanium"],
        "applications": ["Industrial automation", "Assembly fixtures", "Mold positioning", "Automotive hinges", "Precision machinery", "Electronics assembly"],
        "industries": ["Industrial Equipment", "Automotive Industry", "Electronics Industry"],
        "benefits": ["Accurate positioning", "Wear resistance", "Tight tolerance", "Long service life"],
        "seo": ["Precision Dowel Pins", "Steel Dowel Pins", "CNC Pins", "Locating Pins", "Precision Positioning Pins"],
        "related": ["cnc-turning-parts", "precision-shafts", "special-fasteners"],
    },
    {
        "slug": "inserts-thread-parts", "name": "Inserts & Thread Parts",
        "tagline": "Precision threaded inserts and threaded components.",
        "materials": ["Brass", "Stainless Steel", "Aluminum"],
        "applications": ["Plastic injection products", "Consumer electronics", "Medical housings", "Aluminum structures", "Industrial equipment"],
        "industries": ["Electronics Industry", "Medical Devices", "Industrial Equipment"],
        "benefits": ["Excellent thread quality", "Strong retention", "Stable dimensions", "Long service life"],
        "seo": ["Threaded Inserts", "Brass Inserts", "Thread Components", "Custom Thread Parts", "OEM Threaded Parts"],
        "related": ["nuts-threaded-parts", "bolts-studs", "brass-components"],
    },
    {
        "slug": "special-fasteners", "name": "Special Fasteners",
        "tagline": "Custom bolts, screws, studs and fastening solutions.",
        "materials": ["Stainless Steel", "Titanium", "Brass"],
        "applications": ["Industrial machinery", "Automotive", "Aerospace", "Medical equipment", "Electronics"],
        "industries": ["Industrial Equipment", "Automotive Industry", "Aerospace Supply Chain", "Fastener Industry"],
        "benefits": ["Custom dimensions", "Stable quality", "High strength", "OEM production"],
        "seo": ["Custom Fasteners", "Precision Screws", "OEM Bolts", "Special Fasteners", "Custom Studs"],
        "related": ["bolts-studs", "nuts-threaded-parts", "inserts-thread-parts"],
    },
    {
        "slug": "shafts-rods", "name": "Shafts & Rods",
        "tagline": "Precision shafts and rods for motion systems.",
        "materials": ["Stainless Steel", "Aluminum", "Titanium"],
        "applications": ["Motors", "Pumps", "Robotics", "Medical devices", "Electric tools", "Automation"],
        "industries": ["Industrial Equipment", "Medical Devices", "Electronics Industry"],
        "benefits": ["High concentricity", "Smooth surface finish", "Stable machining quality"],
        "seo": ["Precision Shaft", "Motor Shaft", "Steel Shaft", "Linear Shaft", "Custom Shaft"],
        "related": ["precision-shafts", "washers-spacers", "pins-dowels"],
    },
    {
        "slug": "washers-spacers", "name": "Washers & Spacers",
        "tagline": "Precision machined washers and spacers.",
        "materials": ["Stainless Steel", "Aluminum", "Brass"],
        "applications": ["Bearings", "Automotive", "Electronics", "Industrial equipment", "Mechanical assemblies"],
        "industries": ["Industrial Equipment", "Automotive Industry", "Electronics Industry"],
        "benefits": ["Accurate thickness", "Stable assembly", "Reduced vibration"],
        "seo": ["Precision Washer", "Metal Spacer", "Custom Washer", "Machined Spacer"],
        "related": ["shafts-rods", "cnc-turning-parts", "nuts-threaded-parts"],
    },
    {
        "slug": "precision-shafts", "name": "Precision Shafts",
        "tagline": "High precision shafts for servo and motion systems.",
        "materials": ["Stainless Steel", "Titanium"],
        "applications": ["Servo motors", "Robotics", "Automation", "Medical equipment", "Measuring instruments"],
        "industries": ["Industrial Equipment", "Medical Devices"],
        "benefits": ["High concentricity", "Low runout", "Excellent precision"],
        "seo": ["Precision Shaft", "Ground Shaft", "Servo Shaft", "CNC Shaft"],
        "related": ["shafts-rods", "pins-dowels", "cnc-turning-parts"],
    },
    {
        "slug": "bolts-studs", "name": "Bolts & Studs",
        "tagline": "Precision threaded bolts and studs.",
        "materials": ["Stainless Steel", "Titanium", "Brass"],
        "applications": ["Automotive", "Compressors", "Hydraulic equipment", "Industrial machinery"],
        "industries": ["Automotive Industry", "Pneumatic & Hydraulic", "Fastener Industry"],
        "benefits": ["High thread accuracy", "Strong durability", "OEM customization"],
        "seo": ["Precision Bolts", "Threaded Studs", "OEM Bolts", "Custom Studs"],
        "related": ["special-fasteners", "nuts-threaded-parts", "inserts-thread-parts"],
    },
    {
        "slug": "nuts-threaded-parts", "name": "Nuts & Threaded Parts",
        "tagline": "Precision threaded nuts and connectors.",
        "materials": ["Brass", "Stainless Steel"],
        "applications": ["Pneumatic systems", "Hydraulic systems", "Electronics", "Mechanical assemblies"],
        "industries": ["Pneumatic & Hydraulic", "Electronics Industry", "Fastener Industry"],
        "benefits": ["High precision threading", "Excellent fitting", "Stable production"],
        "seo": ["Precision Nuts", "Threaded Parts", "OEM Nuts", "Custom Thread Components"],
        "related": ["bolts-studs", "inserts-thread-parts", "brass-fittings"],
    },
    {
        "slug": "brass-components", "name": "Brass Components",
        "tagline": "Precision brass machined components.",
        "materials": ["Brass", "Copper"],
        "applications": ["RF connectors", "Communication equipment", "Sensors", "Water systems", "Gas systems"],
        "industries": ["Electronics Industry", "Pneumatic & Hydraulic"],
        "benefits": ["Excellent conductivity", "Corrosion resistance", "Beautiful finish"],
        "seo": ["Brass CNC Parts", "Precision Brass Components", "Brass Connectors", "Brass Machining"],
        "related": ["brass-fittings", "precision-connectors", "brass-precision-parts"],
    },
    {
        "slug": "brass-fittings", "name": "Brass Fittings",
        "tagline": "Precision brass fittings for fluid transfer.",
        "materials": ["Brass", "Copper"],
        "applications": ["Pneumatic systems", "Hydraulic systems", "Refrigeration", "Water treatment", "Industrial equipment"],
        "industries": ["Pneumatic & Hydraulic", "Industrial Equipment"],
        "benefits": ["Leak-free sealing", "Corrosion resistance", "Long service life"],
        "seo": ["Brass Fittings", "Hydraulic Fittings", "Pneumatic Fittings", "Custom Brass Fittings"],
        "related": ["brass-components", "nuts-threaded-parts", "brass-precision-parts"],
    },
    {
        "slug": "precision-connectors", "name": "Precision Connectors",
        "tagline": "Precision connector components manufactured by CNC turning.",
        "materials": ["Brass", "Copper", "Stainless Steel"],
        "applications": ["Electronic connectors", "Medical electronics", "Industrial control", "Semiconductor equipment", "Communication equipment"],
        "industries": ["Electronics Industry", "Medical Devices"],
        "benefits": ["Tight tolerance", "Excellent conductivity", "Stable quality"],
        "seo": ["Precision Connectors", "Connector Parts", "Electronic Connectors", "Connector Components"],
        "related": ["brass-precision-parts", "brass-components", "cnc-turning-parts"],
    },
    {
        "slug": "brass-precision-parts", "name": "Brass Precision Parts",
        "tagline": "Small brass precision parts for electronic applications.",
        "materials": ["Brass", "Copper"],
        "applications": ["Electrical terminals", "RF communication", "Sensors", "Battery systems", "Connector assemblies"],
        "industries": ["Electronics Industry"],
        "benefits": ["High conductivity", "Stable dimensions", "Excellent consistency"],
        "seo": ["Brass Precision Parts", "Electrical Components", "Brass Terminal", "Connector Pins"],
        "related": ["precision-connectors", "brass-components", "brass-fittings"],
    },
    {
        "slug": "stainless-steel-parts", "name": "Stainless Steel Parts",
        "tagline": "Precision stainless steel machined components.",
        "materials": ["Stainless Steel"],
        "applications": ["Medical devices", "Food machinery", "Semiconductor equipment", "Industrial automation"],
        "industries": ["Medical Devices", "Industrial Equipment"],
        "benefits": ["Corrosion resistance", "High strength", "Long service life"],
        "seo": ["Stainless Steel CNC Parts", "Medical CNC Parts", "Precision Stainless Components"],
        "related": ["cnc-turning-parts", "precision-shafts", "shafts-rods"],
    },
    {
        "slug": "aluminum-components", "name": "Aluminum Components",
        "tagline": "Precision aluminum machined parts.",
        "materials": ["Aluminum"],
        "applications": ["UAV", "Electronics", "Automotive", "Bicycle", "Aerospace"],
        "industries": ["Aerospace Supply Chain", "Automotive Industry", "Electronics Industry"],
        "benefits": ["Lightweight", "High strength", "Excellent machinability"],
        "seo": ["Aluminum CNC Parts", "Machined Aluminum Components", "Lightweight Precision Parts"],
        "related": ["cnc-turning-parts", "special-fasteners", "washers-spacers"],
    },
]

BY_SLUG = {p["slug"]: p for p in PRODUCTS}

FAQS = [
    ("Can you manufacture parts from our own drawing?",
     "Yes. RI YUE XING is an OEM/ODM manufacturer — we machine to your drawing and specification rather than selling fixed catalog parts. Send us your drawing (2D/3D) and we'll confirm feasibility, materials and tolerances."),
    ("What is the minimum order quantity (MOQ)?",
     "MOQ depends on part complexity, material and tooling requirements. We support both smaller trial orders and stable long-term mass production — contact us with your specification for a tailored quote."),
    ("What materials and tolerances can you work with?",
     "We machine stainless steel, aluminum, brass, copper, titanium and other engineering metals, holding tolerances as tight as ±0.01mm depending on part geometry."),
    ("How is quality verified before shipment?",
     "Every order goes through First Article Inspection (FAI), In-Process Inspection, 100% Final Inspection and CMM measurement against your drawing tolerances."),
]

NAV = """<nav>
  <div class="nav-inner">
    <div class="nav-brand">
      <img src="../assets/logo.png" alt="RI YUE XING logo">
      <div class="nav-logo">RI YUE XING<span>PRECISION INDUSTRIAL</span></div>
    </div>
    <div class="nav-links">
      <a href="../index.html#about">About</a>
      <a href="../index.html#capabilities">Capabilities</a>
      <a href="index.html">Products</a>
      <a href="../index.html#industries">Industries</a>
      <a href="../index.html#contact" class="nav-cta">Contact Us</a>
    </div>
  </div>
</nav>"""

FOOTER = """<footer>
  <strong>RI YUE XING PRECISION INDUSTRIAL CO., LTD.</strong>（日月星精密工業有限公司）｜ Kaohsiung, Taiwan, since 1987<br>
  © 2026 RI YUE XING Precision Industrial. All rights reserved.
  <div class="foot-links"><a href="../index.html">Home</a>｜<a href="index.html">All Products</a>｜<a href="../index.html#contact">Contact</a></div>
</footer>"""

CONTACT_SECTION = """<section id="contact">
  <div class="container">
    <div class="section-header">
      <div class="eyebrow">Get In Touch</div>
      <h2>Request a Quote for This Product</h2>
      <p>Send us your drawing and specification — our team responds within 1–2 business days.</p>
    </div>
    <div class="contact-grid">
      <div class="contact-card">
        <div class="contact-icon">&#9993;&#65039;</div>
        <h3>Email</h3>
        <p>scnc3499@gmail.com</p>
        <a class="btn-inline" href="mailto:scnc3499@gmail.com?subject=RFQ%20Inquiry%20-%20RI%20YUE%20XING">Send Email</a>
      </div>
      <div class="contact-card">
        <div class="contact-icon">&#128172;</div>
        <h3>WhatsApp</h3>
        <p>Andrea from RI YUE XING<br>+886 987 860 149</p>
        <a class="btn-inline" href="https://wa.me/886987860149?text=Hi%20Andrea%2C%20I%27d%20like%20to%20request%20a%20quote." target="_blank" rel="noopener">Chat on WhatsApp</a>
      </div>
      <div class="contact-card">
        <div class="contact-icon">&#128222;</div>
        <h3>Phone / Fax</h3>
        <p>TEL +886-7-701-3498<br>FAX +886-7-701-9649</p>
        <a class="btn-inline" href="tel:+88677013498">Call Now</a>
      </div>
    </div>
  </div>
</section>"""


def tag_list(items):
    return "".join(f'<span class="tag">{x}</span>' for x in items)


def li_list(items):
    return "".join(f"<li>{x}</li>" for x in items)


def render_product_page(p):
    related_html = "".join(
        f'<a class="related-card" href="{r}.html">{BY_SLUG[r]["name"]}</a>' for r in p["related"] if r in BY_SLUG
    )
    faq_html = "".join(
        f'<div class="faq-item"><h4>{q}</h4><p>{a}</p></div>' for q, a in FAQS
    )
    title = f'{p["name"]} | OEM CNC Machining Taiwan | RI YUE XING'
    desc = f'{p["tagline"]} Precision CNC machined {p["name"].lower()} manufactured in Taiwan since 1987. Materials: {", ".join(p["materials"])}. Tolerance ±0.01mm.'
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{', '.join(p['seo'])}">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>

{NAV}

<div class="breadcrumb"><div class="container"><a href="../index.html">Home</a> / <a href="index.html">Products</a> / {p["name"]}</div></div>

<header class="page-hero">
  <div class="eyebrow">Product Category</div>
  <h1>{p["name"]}</h1>
  <p>{p["tagline"]}</p>
</header>

<section>
  <div class="detail-grid">
    <div class="detail-block">
      <h2>Product Overview</h2>
      <p>{p["tagline"]} As an OEM/ODM precision CNC machining manufacturer, RI YUE XING produces {p["name"].lower()} strictly to customer drawings and specifications — not as standard catalog products. Every part becomes a critical component inside our customers' finished products.</p>

      <h2>Features & Customer Benefits</h2>
      <ul>{li_list(p["benefits"])}</ul>

      <h2>Manufacturing Capabilities</h2>
      <p>Manufactured using Swiss-type CNC turning, CNC turning, CNC milling and 5-axis machining as required, with precision secondary processing (plating, polishing, deburring). See our full <a href="../index.html#capabilities">manufacturing capabilities</a>.</p>

      <h2>Typical Applications</h2>
      <ul>{li_list(p["applications"])}</ul>

      <h2>Quality Assurance</h2>
      <p>Every batch is verified through First Article Inspection (FAI), In-Process Inspection, 100% Final Inspection and CMM measurement against your drawing tolerances before shipment.</p>

      <h2>Frequently Asked Questions</h2>
      {faq_html}
    </div>
    <div>
      <div class="side-card">
        <h3>Materials Available</h3>
        {tag_list(p["materials"])}
      </div>
      <div class="side-card">
        <h3>Industries Served</h3>
        {tag_list(p["industries"])}
      </div>
      <div class="side-card">
        <h3>Why Choose RI YUE XING</h3>
        <ul style="list-style:none;">
          <li style="padding:4px 0;font-size:0.86rem;color:#414d5e;">✓ Established since 1987, Made in Taiwan</li>
          <li style="padding:4px 0;font-size:0.86rem;color:#414d5e;">✓ OEM / ODM manufacturing</li>
          <li style="padding:4px 0;font-size:0.86rem;color:#414d5e;">✓ ±0.01mm tolerance capability</li>
          <li style="padding:4px 0;font-size:0.86rem;color:#414d5e;">✓ Flexible MOQ, stable mass production</li>
          <li style="padding:4px 0;font-size:0.86rem;color:#414d5e;">✓ Long-term manufacturing partner</li>
        </ul>
      </div>
      <a href="../index.html#contact" class="btn btn-primary" style="display:block;text-align:center;background:#c9a44c;color:#0b2545;">Request a Quote</a>
    </div>
  </div>
</section>

<section style="background:#f7f9fc;">
  <div class="section-header">
    <div class="eyebrow">Related Products</div>
    <h2>You May Also Need</h2>
  </div>
  <div class="related-grid">
    {related_html}
  </div>
</section>

{CONTACT_SECTION}

{FOOTER}

</body>
</html>
"""
    path = os.path.join(OUT_DIR, f"{p['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


def render_hub():
    cards = ""
    for p in PRODUCTS:
        cards += f"""<a class="hub-card" href="{p['slug']}.html">
      <h3>{p['name']}</h3>
      <p>{p['tagline']}</p>
      <div class="tags">{tag_list(p['materials'][:3])}</div>
      <div class="more" style="margin-top:12px;">View Details →</div>
    </a>
"""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Products | OEM CNC Precision Machined Components | RI YUE XING</title>
<meta name="description" content="Full range of RI YUE XING's OEM/ODM precision CNC machined components: turning parts, pins, inserts, fasteners, shafts, brass and stainless steel parts, manufactured in Taiwan since 1987.">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>

{NAV}

<div class="breadcrumb"><div class="container"><a href="../index.html">Home</a> / Products</div></div>

<header class="page-hero">
  <div class="eyebrow">Product Range</div>
  <h1>Precision CNC Machined Components</h1>
  <p>15 product categories, manufactured to customer drawings — not sold as standard catalog parts. Ø1mm to Ø20mm, ±0.01mm tolerance, OEM/ODM production since 1987.</p>
</header>

<section>
  <div class="product-hub-grid">
    {cards}
  </div>
</section>

{CONTACT_SECTION}

{FOOTER}

</body>
</html>
"""
    path = os.path.join(OUT_DIR, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


if __name__ == "__main__":
    for p in PRODUCTS:
        print(render_product_page(p))
    print(render_hub())
    print(f"Generated {len(PRODUCTS)} product pages + hub")
