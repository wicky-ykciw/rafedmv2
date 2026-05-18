# -*- coding: utf-8 -*-
from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# 1. Update header with revision notice
old_p = '<p>Promotion Period: 15 May 2026 00:00:00 – 30 June 2026 23:59:59 (MT4/MT5 Time) · Eligible Regions: Excluding Vietnam · T&C: VFSC 40356 · 7 Emails · IB Pitch removed per compliance</p>'

new_p = '''<p style="color: #EF4444; font-weight: 600; margin-bottom: 8px;">🔄 REVISED VERSION — v2.1 Updates: Global lot replacements (1→5), $50→$25 pricing, language-specific content rewrites</p>
      <p style="margin-bottom: 8px;">Promotion Period: 15 May 2026 00:00:00 – 30 June 2026 23:59:59 (MT4/MT5 Time) · Eligible Regions: Excluding Vietnam · T&C: VFSC 40356 · 7 Emails · IB Pitch removed per compliance</p>
      <p style="color: #DC2626; font-weight: 600; font-size: 11px;">⚠️ NOTICE: Vietnamese (VN) language variant is decommissioned and will be removed. Please do not use VN content.</p>'''

if old_p in text:
    text = text.replace(old_p, new_p, 1)
    print("✓ Updated header with revision notice and VN decommission alert")
else:
    print("✗ Could not find header paragraph")

# 2. Apply strikethrough to all VN email sections
# Find and wrap all email VN sections with strikethrough styling
vn_email_ids = [
    'email1-vn', 'email2-vn', 'email3-vn', 'email4-vn', 
    'email5-vn', 'email6-vn', 'email7-vn'
]

count_vn_updated = 0
for vn_id in vn_email_ids:
    # Find the VN email div and wrap it with strikethrough
    old_div = f'  <div id="{vn_id}" class="lang-content">'
    new_div = f'  <div id="{vn_id}" class="lang-content" style="text-decoration: line-through; opacity: 0.5; background-color: #FEF2F2; border-left: 3px solid #DC2626; padding-left: 16px;">'
    
    if old_div in text:
        text = text.replace(old_div, new_div, 1)
        count_vn_updated += 1
        print(f"✓ Applied strikethrough to {vn_id}")
    else:
        print(f"✗ Could not find {vn_id}")

print(f"\nVN sections strikethrough applied: {count_vn_updated}/7")

# 3. Update title with revision indicator color
old_title = '<h1>Q2 2026 Refer-A-Friend — EDM Content Hub (v2)</h1>'
new_title = '<h1 style="color: #DC2626;">Q2 2026 Refer-A-Friend — EDM Content Hub <span style="color: #10B981;">(v2.1 REVISED)</span></h1>'

if old_title in text:
    text = text.replace(old_title, new_title, 1)
    print("✓ Updated title with revision indicator")
else:
    print("✗ Could not find title")

path.write_text(text, encoding='utf-8')
print("\n✅ All formatting updates completed successfully!")
