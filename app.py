import streamlit as st
import re
import json
import requests
from typing import Dict, List, Any
import time
from datetime import datetime
import google.generativeai as genai

# Configure Gemini API
class GeminiWebsiteGenerator:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
    def generate_website_structure(self, user_prompt: str, color_scheme: str = "primary", layout_type: str = "default") -> Dict[str, Any]:
        """Generate website structure using Gemini 2.0 Flash with enhanced thinking"""
        
        system_prompt = f"""
        You are an expert web developer and UI/UX designer specializing in CampEd UI components. 
        Generate a complete, modern website structure based on user input using ONLY CampEd UI components.
        
        Think step by step about:
        1. What type of website this is
        2. What sections would be most effective
        3. How to organize content logically
        4. Which CampEd UI components best serve each purpose
        5. How to make it visually appealing and functional
        
        Available CampEd UI Components:
        - Button: Primary, Secondary, Outline, Ghost variants (with hover effects)
        - Card: With header, content, footer (supports images and actions)
        - Typography: Heading (h1-h6), Paragraph, Small text (with proper hierarchy)
        - Navigation: Menu, Breadcrumb (responsive and accessible)
        - Form: Input, Textarea, Select, Checkbox, Radio (with validation states)
        - Alert: Success, Error, Warning, Info (with icons)
        - Badge: Default, Secondary, Destructive, Outline (for status indicators)
        - Dialog: Modal, Drawer (for interactions)
        - Tabs: Horizontal, Vertical (for content organization)
        - Separator: Horizontal, Vertical (for visual breaks)
        - Avatar: Image, Fallback (for user representation)
        - Progress: Linear, Circular (for loading states)
        - Skeleton: Loading states (for better UX)
        - Grid: Responsive layouts (2, 3, 4 columns)
        - Hero: Large impact sections
        - Gallery: Image showcases
        - Testimonials: Customer feedback
        - FAQ: Collapsible question sections
        
        IMPORTANT: Use color scheme "{color_scheme}" and layout type "{layout_type}".
        
        Always respond with valid JSON structure containing:
        {{
            "title": "Website title",
            "description": "Meta description",
            "sections": [
                {{
                    "type": "hero|navigation|content|cards|contact|footer|gallery|testimonials|faq|features",
                    "title": "Section title",
                    "content": "Section content",
                    "components": ["component1", "component2"],
                    "props": {{
                        "variant": "primary|secondary|outline",
                        "size": "sm|md|lg",
                        "color": "{color_scheme}",
                        "layout": "{layout_type}",
                        "cards": [
                            {{
                                "title": "Card title",
                                "content": "Card description",
                                "image": "placeholder-url",
                                "footer": "Card footer with actions"
                            }}
                        ],
                        "links": [
                            {{
                                "text": "Link text",
                                "href": "#section"
                            }}
                        ],
                        "fields": [
                            {{
                                "type": "text|email|tel|textarea",
                                "name": "field_name",
                                "label": "Field Label",
                                "placeholder": "Enter..."
                            }}
                        ]
                    }}
                }}
            ],
            "color_scheme": "{color_scheme}",
            "layout": "{layout_type}"
        }}
        
        Make the website modern, accessible, and fully functional. Include realistic content and proper component usage.
        """
        
        try:
            response = self.model.generate_content(
                f"{system_prompt}\n\nUser Request: {user_prompt}",
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    top_p=0.9,
                    max_output_tokens=4096,
                )
            )
            
            # Parse JSON response
            response_text = response.text.strip()
            if response_text.startswith('```json'):
                response_text = response_text[7:-3]
            elif response_text.startswith('```'):
                response_text = response_text[3:-3]
                
            parsed_structure = json.loads(response_text)
            
            # Ensure color scheme and layout are applied
            parsed_structure["color_scheme"] = color_scheme
            parsed_structure["layout"] = layout_type
            
            return parsed_structure
            
        except Exception as e:
            st.error(f"Gemini API Error: {str(e)}")
            return self._get_fallback_structure(user_prompt, color_scheme, layout_type)
    
    def _get_fallback_structure(self, prompt: str, color_scheme: str, layout_type: str) -> Dict[str, Any]:
        """Enhanced fallback structure when API fails"""
        return {
            "title": "AI Generated Website",
            "description": f"Generated using CampEd UI components with {color_scheme} theme",
            "sections": [
                {
                    "type": "navigation",
                    "title": "Navigation",
                    "content": "",
                    "components": ["Navigation"],
                    "props": {
                        "links": [
                            {"text": "Home", "href": "#home"},
                            {"text": "About", "href": "#about"},
                            {"text": "Services", "href": "#services"},
                            {"text": "Contact", "href": "#contact"}
                        ]
                    }
                },
                {
                    "type": "hero",
                    "title": "Welcome to Your AI Website",
                    "content": "This website was generated using advanced AI and CampEd UI components",
                    "components": ["Button", "Typography"],
                    "props": {"variant": color_scheme, "size": "lg"}
                },
                {
                    "type": "features",
                    "title": "Key Features",
                    "content": "Discover what makes us special",
                    "components": ["Card", "Grid"],
                    "props": {
                        "cards": [
                            {
                                "title": "Modern Design",
                                "content": "Built with the latest design principles",
                                "footer": "Learn More"
                            },
                            {
                                "title": "Responsive",
                                "content": "Works perfectly on all devices",
                                "footer": "View Demo"
                            },
                            {
                                "title": "Fast Loading",
                                "content": "Optimized for speed and performance",
                                "footer": "Test Speed"
                            }
                        ]
                    }
                },
                {
                    "type": "contact",
                    "title": "Get In Touch",
                    "content": "We'd love to hear from you",
                    "components": ["Form", "Button"],
                    "props": {
                        "fields": [
                            {"type": "text", "name": "name", "label": "Full Name", "placeholder": "Enter your name"},
                            {"type": "email", "name": "email", "label": "Email", "placeholder": "Enter your email"},
                            {"type": "textarea", "name": "message", "label": "Message", "placeholder": "Your message"}
                        ]
                    }
                }
            ],
            "color_scheme": color_scheme,
            "layout": layout_type
        }

class CampEdUIGenerator:
    """Enhanced CampEd UI Component Generator with real styling"""
    
    def __init__(self):
        self.base_cdn = "https://cdn.jsdelivr.net/npm/@camped/ui@latest"
        
    def get_camped_css(self, color_scheme: str = "primary") -> str:
        """Get enhanced CampEd UI CSS with color schemes"""
        
        color_vars = {
            "primary": {
                "primary": "#2563eb",
                "primary-foreground": "#ffffff",
                "accent": "#1d4ed8"
            },
            "secondary": {
                "primary": "#64748b", 
                "primary-foreground": "#ffffff",
                "accent": "#475569"
            },
            "accent": {
                "primary": "#f59e0b",
                "primary-foreground": "#ffffff", 
                "accent": "#d97706"
            }
        }
        
        colors = color_vars.get(color_scheme, color_vars["primary"])
        
        return f"""
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <style>
        /* CampEd UI Enhanced Styles */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        :root {{
            --camped-primary: {colors["primary"]};
            --camped-primary-foreground: {colors["primary-foreground"]};
            --camped-accent: {colors["accent"]};
            --camped-secondary: #64748b;
            --camped-secondary-foreground: #ffffff;
            --camped-muted: #f1f5f9;
            --camped-muted-foreground: #64748b;
            --camped-destructive: #ef4444;
            --camped-destructive-foreground: #ffffff;
            --camped-border: #e2e8f0;
            --camped-input: #ffffff;
            --camped-ring: var(--camped-primary);
            --camped-background: #ffffff;
            --camped-foreground: #0f172a;
            --camped-card: #ffffff;
            --camped-card-foreground: #0f172a;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: var(--camped-foreground);
            background: var(--camped-background);
        }}
        
        .camped-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }}
        
        .camped-section {{
            padding: 4rem 0;
        }}
        
        .camped-grid {{
            display: grid;
            gap: 2rem;
        }}
        
        .camped-grid-2 {{ grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }}
        .camped-grid-3 {{ grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }}
        .camped-grid-4 {{ grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }}
        
        /* Navigation */
        .camped-navigation {{
            background: var(--camped-background);
            border-bottom: 1px solid var(--camped-border);
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
            backdrop-filter: blur(10px);
        }}
        
        .camped-nav-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .camped-nav__brand {{
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--camped-primary);
        }}
        
        .camped-nav__menu {{
            display: flex;
            gap: 2rem;
        }}
        
        .camped-nav__link {{
            text-decoration: none;
            color: var(--camped-foreground);
            font-weight: 500;
            transition: color 0.2s;
        }}
        
        .camped-nav__link:hover {{
            color: var(--camped-primary);
        }}
        
        /* Buttons */
        .camped-button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.5rem 1rem;
            border: 1px solid transparent;
            border-radius: 0.375rem;
            font-weight: 500;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 0.875rem;
        }}
        
        .camped-button--default {{
            background: var(--camped-primary);
            color: var(--camped-primary-foreground);
        }}
        
        .camped-button--default:hover {{
            background: var(--camped-accent);
            transform: translateY(-1px);
        }}
        
        .camped-button--outline {{
            border-color: var(--camped-primary);
            color: var(--camped-primary);
            background: transparent;
        }}
        
        .camped-button--outline:hover {{
            background: var(--camped-primary);
            color: var(--camped-primary-foreground);
        }}
        
        .camped-button--lg {{
            padding: 0.75rem 2rem;
            font-size: 1rem;
        }}
        
        /* Cards */
        .camped-card {{
            background: var(--camped-card);
            border: 1px solid var(--camped-border);
            border-radius: 0.5rem;
            overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        
        .camped-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }}
        
        .camped-card__header {{
            padding: 1.5rem 1.5rem 0;
        }}
        
        .camped-card__title {{
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--camped-card-foreground);
            margin-bottom: 0.5rem;
        }}
        
        .camped-card__content {{
            padding: 0 1.5rem 1.5rem;
        }}
        
        .camped-card__description {{
            color: var(--camped-muted-foreground);
            line-height: 1.5;
        }}
        
        .camped-card__footer {{
            padding: 1rem 1.5rem;
            background: var(--camped-muted);
            border-top: 1px solid var(--camped-border);
        }}
        
        /* Typography */
        .camped-typography--h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 1rem;
        }}
        
        .camped-typography--h2 {{
            font-size: 2rem;
            font-weight: 600;
            line-height: 1.3;
            margin-bottom: 1rem;
        }}
        
        .camped-typography--p {{
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 1rem;
            color: var(--camped-muted-foreground);
        }}
        
        /* Hero Section */
        .camped-hero {{
            background: linear-gradient(135deg, var(--camped-primary), var(--camped-accent));
            color: white;
            text-align: center;
            padding: 6rem 0;
        }}
        
        .camped-hero__content {{
            max-width: 800px;
            margin: 0 auto;
        }}
        
        .camped-hero h1 {{
            color: white;
            font-size: 3rem;
            margin-bottom: 1rem;
        }}
        
        .camped-hero p {{
            color: rgba(255,255,255,0.9);
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }}
        
        .camped-hero__actions {{
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }}
        
        /* Forms */
        .camped-form {{
            max-width: 500px;
            margin: 0 auto;
        }}
        
        .camped-form__group {{
            margin-bottom: 1.5rem;
        }}
        
        .camped-label {{
            display: block;
            font-weight: 500;
            margin-bottom: 0.5rem;
            color: var(--camped-foreground);
        }}
        
        .camped-input, .camped-textarea {{
            width: 100%;
            padding: 0.75rem;
            border: 1px solid var(--camped-border);
            border-radius: 0.375rem;
            font-size: 1rem;
            transition: border-color 0.2s, box-shadow 0.2s;
        }}
        
        .camped-input:focus, .camped-textarea:focus {{
            outline: none;
            border-color: var(--camped-primary);
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
        }}
        
        .camped-textarea {{
            min-height: 120px;
            resize: vertical;
        }}
        
        .camped-form__actions {{
            text-align: center;
            margin-top: 2rem;
        }}
        
        /* Responsive Design */
        @media (max-width: 768px) {{
            .camped-section {{ padding: 2rem 0; }}
            .camped-grid {{ gap: 1rem; }}
            .camped-hero h1 {{ font-size: 2rem; }}
            .camped-nav__menu {{ 
                flex-direction: column;
                gap: 1rem;
            }}
            .camped-hero__actions {{
                flex-direction: column;
                align-items: center;
            }}
        }}
        
        /* Animations */
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .fade-in-up {{
            animation: fadeInUp 0.6s ease-out;
        }}
        </style>
        """
    
    def generate_button(self, text: str, variant: str = "default", size: str = "default") -> str:
        """Generate CampEd UI Button with enhanced styling"""
        return f'<button class="camped-button camped-button--{variant} camped-button--{size}">{text}</button>'
    
    def generate_card(self, title: str, content: str, footer: str = "") -> str:
        """Generate CampEd UI Card with enhanced styling"""
        footer_html = f'<div class="camped-card__footer">{footer}</div>' if footer else ''
        return f'''
        <div class="camped-card fade-in-up">
            <div class="camped-card__header">
                <h3 class="camped-card__title">{title}</h3>
            </div>
            <div class="camped-card__content">
                <p class="camped-card__description">{content}</p>
            </div>
            {footer_html}
        </div>
        '''
    
    def generate_typography(self, text: str, variant: str = "p") -> str:
        """Generate CampEd UI Typography"""
        return f'<{variant} class="camped-typography--{variant}">{text}</{variant}>'
    
    def generate_navigation(self, brand: str, links: List[Dict[str, str]]) -> str:
        """Generate CampEd UI Navigation with enhanced styling"""
        nav_items = ""
        for link in links:
            nav_items += f'<a href="{link.get("href", "#")}" class="camped-nav__link">{link.get("text", "")}</a>'
        
        return f'''
        <nav class="camped-navigation">
            <div class="camped-container">
                <div class="camped-nav-container">
                    <div class="camped-nav__brand">{brand}</div>
                    <div class="camped-nav__menu">
                        {nav_items}
                    </div>
                </div>
            </div>
        </nav>
        '''
    
    def generate_hero(self, title: str, subtitle: str, cta_text: str = "Get Started") -> str:
        """Generate CampEd UI Hero Section with enhanced styling"""
        return f'''
        <section class="camped-hero">
            <div class="camped-container">
                <div class="camped-hero__content fade-in-up">
                    {self.generate_typography(title, "h1")}
                    {self.generate_typography(subtitle, "p")}
                    <div class="camped-hero__actions">
                        {self.generate_button(cta_text, "default", "lg")}
                        {self.generate_button("Learn More", "outline", "lg")}
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def generate_form(self, fields: List[Dict[str, str]]) -> str:
        """Generate CampEd UI Form with enhanced styling"""
        form_fields = ""
        for field in fields:
            field_type = field.get("type", "text")
            field_name = field.get("name", "")
            field_label = field.get("label", "")
            field_placeholder = field.get("placeholder", "")
            
            if field_type == "textarea":
                form_fields += f'''
                <div class="camped-form__group">
                    <label class="camped-label" for="{field_name}">{field_label}</label>
                    <textarea class="camped-textarea" id="{field_name}" name="{field_name}" placeholder="{field_placeholder}"></textarea>
                </div>
                '''
            else:
                form_fields += f'''
                <div class="camped-form__group">
                    <label class="camped-label" for="{field_name}">{field_label}</label>
                    <input class="camped-input" type="{field_type}" id="{field_name}" name="{field_name}" placeholder="{field_placeholder}">
                </div>
                '''
        
        return f'''
        <form class="camped-form">
            {form_fields}
            <div class="camped-form__actions">
                {self.generate_button("Submit", "default", "lg")}
            </div>
        </form>
        '''
    
    def generate_website(self, structure: Dict[str, Any]) -> str:
        """Generate complete website HTML with enhanced features"""
        sections_html = ""
        color_scheme = structure.get("color_scheme", "primary")
        
        for section in structure.get("sections", []):
            section_type = section.get("type", "content")
            section_title = section.get("title", "")
            section_content = section.get("content", "")
            section_props = section.get("props", {})
            
            if section_type == "hero":
                sections_html += self.generate_hero(section_title, section_content)
                
            elif section_type == "navigation":
                links = section_props.get("links", [])
                sections_html += self.generate_navigation(section_title, links)
                
            elif section_type == "cards" or section_type == "features":
                cards = section_props.get("cards", [])
                cards_html = ""
                for card in cards:
                    cards_html += self.generate_card(
                        card.get("title", ""),
                        card.get("content", ""),
                        card.get("footer", "")
                    )
                sections_html += f'''
                <section class="camped-section">
                    <div class="camped-container">
                        {self.generate_typography(section_title, "h2")}
                        <div class="camped-grid camped-grid-3">
                            {cards_html}
                        </div>
                    </div>
                </section>
                '''
                
            elif section_type == "contact":
                fields = section_props.get("fields", [])
                sections_html += f'''
                <section class="camped-section">
                    <div class="camped-container">
                        {self.generate_typography(section_title, "h2")}
                        <p class="camped-typography--p" style="text-align: center; margin-bottom: 3rem;">{section_content}</p>
                        {self.generate_form(fields)}
                    </div>
                </section>
                '''
                
            else:  # content section
                sections_html += f'''
                <section class="camped-section">
                    <div class="camped-container">
                        {self.generate_typography(section_title, "h2")}
                        {self.generate_typography(section_content, "p")}
                    </div>
                </section>
                '''
        
        # Complete HTML document
        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{structure.get("title", "AI Generated Website")}</title>
            <meta name="description" content="{structure.get("description", "")}">
            {self.get_camped_css(color_scheme)}
        </head>
        <body>
            {sections_html}
            <footer class="camped-section" style="background: var(--camped-muted); text-align: center;">
                <div class="camped-container">
                    <p class="camped-typography--p">© 2024 Generated with CampEd UI & Gemini AI • Built with ❤️</p>
                </div>
            </footer>
        </body>
        </html>
        '''

# Enhanced Templates
def get_enhanced_templates():
    return {
        "Custom": "",
        "Tech Startup": """Create a modern tech startup landing page for an AI-powered productivity tool. 
        Include: compelling hero section with product demo CTA, key features showcase with icons, 
        customer testimonials, pricing tiers, team section with photos, and contact form. 
        Use modern gradients and clean design.""",
        
        "Portfolio": """Design a creative portfolio website for a UI/UX designer. 
        Include: striking hero with personal brand, featured projects gallery with case studies, 
        skills and expertise section, client testimonials, about section with personal story, 
        and contact form with social links. Make it visually impressive.""",
        
        "Restaurant": """Build an elegant restaurant website for fine dining establishment. 
        Include: appetizing hero with reservation CTA, menu categories with prices, 
        image gallery of dishes and ambiance, chef's story section, customer reviews, 
        location with hours, and reservation booking form.""",
        
        "E-commerce": """Generate a modern e-commerce store for sustainable fashion brand. 
        Include: product showcase hero, featured categories, best sellers grid, 
        sustainability story section, customer reviews, newsletter signup, 
        and shopping features like wishlist and cart.""",
        
        "Blog": """Create a professional blog website for technology insights. 
        Include: featured article hero, latest posts grid with thumbnails, 
        category navigation, author bio section, newsletter subscription, 
        search functionality, and comment system.""",
        
        "Agency": """Build a digital marketing agency website with premium feel. 
        Include: results-focused hero, services showcase with icons, case studies grid, 
        team member profiles, client logos section, success statistics, 
        and lead generation contact form.""",
        
        "SaaS Platform": """Design a SaaS platform landing page for project management tool.
        Include: problem-solution hero, feature comparison table, integration showcase,
        customer success stories, pricing plans, free trial CTA, and demo booking form.""",
        
        "Educational": """Create an online learning platform website for coding bootcamp.
        Include: inspiring hero with enrollment CTA, course catalog with difficulty levels,
        instructor profiles, student success stories, curriculum overview,
        and application form with scholarship info."""
    }

# Streamlit App with Enhanced Features
def main():
    st.set_page_config(
        page_title="CampEd UI AI Generator",
        page_icon="🚀",
        layout="wide"
    )
    
    # Initialize session state
    if 'generation_count' not in st.session_state:
        st.session_state.generation_count = 0
    if 'last_settings' not in st.session_state:
        st.session_state.last_settings = {}
    
    st.title("🚀 PromptPixel-You give the prompt, we paint the pixels.")
    st.markdown("**Real-time AI-powered website generation using Google Gemini 2.0 Flash & CampEd UI**")
    
    # API Configuration
    with st.sidebar:
        st.header("🔧 Configuration")
        
        # Google Gemini API Key
        api_key = st.text_input(
            "Google Gemini API Key",
            type="password",
            help="Get your API key from Google AI Studio",
            placeholder="Enter your Gemini API key..."
        )
        
        if not api_key:
            st.warning("⚠️ Please enter your Gemini API key to continue")
            st.info("💡 Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)")
            st.stop()
        
        st.success("✅ API Key Configured")
        
        # Model Parameters
        st.subheader("🤖 AI Model Settings")
        temperature = st.slider(
            "Creativity Level", 
            0.1, 1.0, 0.7, 0.1,
            help="Higher values = more creative, Lower values = more focused"
        )
        
        # CampEd UI Settings
        st.subheader("🎨 Design Settings")
        color_scheme = st.selectbox(
            "Color Scheme", 
            ["primary", "secondary", "accent"],
            help="Choose the main color theme"
        )
        
        layout_type = st.selectbox(
            "Layout Style", 
            ["default", "centered", "wide"],
            help="Choose the overall layout approach"
        )
        
        # Real-time Generation
        st.subheader("⚡ Generation Mode")
        realtime_mode = st.checkbox(
            "Enable Real-time Generation", 
            value=True,
            help="Generate as you type (requires API key)"
        )
        
        if realtime_mode:
            st.success("🔄 Real-time mode active")
            generation_delay = st.slider(
                "Generation Delay (seconds)", 
                0.5, 3.0, 1.0, 0.5,
                help="Delay before auto-generation triggers"
            )
        else:
            st.info("💡 Manual generation mode")
        
        # Generation Statistics
        st.subheader("📊 Statistics")
        st.metric("Total Generations", st.session_state.generation_count)
        
        if st.button("🔄 Reset Stats"):
            st.session_state.generation_count = 0
            st.rerun()

    # Main Interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("✍️ Website Description")
        
        # Template Selection
        templates = get_enhanced_templates()
        selected_template = st.selectbox(
            "Choose Template",
            list(templates.keys()),
            help="Select a template or choose 'Custom' for your own idea"
        )
        
        # User Input
        if selected_template == "Custom":
            user_prompt = st.text_area(
                "Describe your website:",
                height=200,
                placeholder="Describe the website you want to create...\nExample: A modern fitness app landing page with workout plans, trainer profiles, and membership signup",
                help="Be specific about the type of website, key sections, and features you want"
            )
        else:
            user_prompt = st.text_area(
                f"Template: {selected_template}",
                value=templates[selected_template],
                height=200,
                help="You can modify this template description or use it as-is"
            )
        
        # Enhancement Options
        st.subheader("🎯 Enhancement Options")
        col_a, col_b = st.columns(2)
        
        with col_a:
            include_animations = st.checkbox("✨ Animations", value=True)
            include_icons = st.checkbox("🎨 Icons", value=True)
            responsive_design = st.checkbox("📱 Mobile-First", value=True)
        
        with col_b:
            modern_gradients = st.checkbox("🌈 Modern Gradients", value=True)
            interactive_elements = st.checkbox("🖱️ Interactive Elements", value=True)
            accessibility_features = st.checkbox("♿ Accessibility", value=True)
        
        # Advanced Settings
        with st.expander("⚙️ Advanced Settings"):
            max_sections = st.slider("Max Sections", 3, 10, 6)
            content_depth = st.select_slider(
                "Content Detail Level",
                options=["Minimal", "Standard", "Detailed", "Comprehensive"],
                value="Standard"
            )
            include_placeholder_images = st.checkbox("🖼️ Placeholder Images", value=True)
    
    with col2:
        st.header("🎨 Live Preview & Generation")
        
        # Initialize generators
        if api_key:
            gemini_generator = GeminiWebsiteGenerator(api_key)
            ui_generator = CampEdUIGenerator()
        
        # Real-time generation logic
        current_settings = {
            'prompt': user_prompt,
            'template': selected_template,
            'color_scheme': color_scheme,
            'layout_type': layout_type,
            'temperature': temperature,
            'enhancements': {
                'animations': include_animations,
                'icons': include_icons,
                'responsive': responsive_design,
                'gradients': modern_gradients,
                'interactive': interactive_elements,
                'accessibility': accessibility_features
            }
        }
        
        # Check if settings changed for real-time mode
        settings_changed = current_settings != st.session_state.last_settings
        should_generate = False
        
        if realtime_mode and settings_changed and user_prompt.strip():
            if 'last_generation_time' not in st.session_state:
                st.session_state.last_generation_time = 0
            
            current_time = time.time()
            if current_time - st.session_state.last_generation_time > generation_delay:
                should_generate = True
                st.session_state.last_generation_time = current_time
        
        # Manual generation button
        manual_generate = st.button(
            "🚀 Generate Website", 
            type="primary",
            disabled=not user_prompt.strip(),
            help="Generate your website based on the description"
        )
        
        if should_generate or manual_generate:
            if user_prompt.strip():
                with st.spinner("🤖 AI is crafting your website..."):
                    # Enhanced prompt with user preferences
                    enhanced_prompt = f"""
                    {user_prompt}
                    
                    Additional Requirements:
                    - Include {max_sections} main sections maximum
                    - Content detail level: {content_depth}
                    - {'Include animations and transitions' if include_animations else 'Minimal animations'}
                    - {'Use Font Awesome icons' if include_icons else 'Text-only elements'}
                    - {'Mobile-first responsive design' if responsive_design else 'Desktop-focused'}
                    - {'Modern gradients and visual effects' if modern_gradients else 'Flat design'}
                    - {'Interactive hover effects and micro-interactions' if interactive_elements else 'Static elements'}
                    - {'WCAG accessibility compliance' if accessibility_features else 'Basic accessibility'}
                    - {'Include placeholder images with proper alt text' if include_placeholder_images else 'Text-only content'}
                    
                    Make it professional, modern, and fully functional with real CampEd UI components.
                    """
                    
                    try:
                        # Generate structure
                        structure = gemini_generator.generate_website_structure(
                            enhanced_prompt, 
                            color_scheme, 
                            layout_type
                        )
                        
                        # Generate HTML
                        website_html = ui_generator.generate_website(structure)
                        
                        # Update session state
                        st.session_state.generation_count += 1
                        st.session_state.last_settings = current_settings
                        st.session_state.current_website = website_html
                        st.session_state.current_structure = structure
                        
                        st.success(f"✅ Website generated successfully! (Generation #{st.session_state.generation_count})")
                        
                        # Display structure info
                        with st.expander("📋 Website Structure"):
                            st.json(structure)
                        
                    except Exception as e:
                        st.error(f"❌ Generation failed: {str(e)}")
        
        # Display generated website
        if 'current_website' in st.session_state:
            st.subheader("🌐 Your Generated Website")
            
            # Tabs for different views
            tab1, tab2, tab3 = st.tabs(["🖥️ Preview", "📝 HTML Code", "⚙️ Structure"])
            
            with tab1:
                st.components.v1.html(
                    st.session_state.current_website,
                    height=800,
                    scrolling=True
                )
            
            with tab2:
                st.code(st.session_state.current_website, language='html')
                if st.button("📋 Copy HTML"):
                    st.code(st.session_state.current_website)
                    st.success("Code displayed above - copy manually")
            
            with tab3:
                if 'current_structure' in st.session_state:
                    st.json(st.session_state.current_structure)
            
            # Download options
            st.subheader("💾 Download Options")
            col_dl1, col_dl2, col_dl3 = st.columns(3)
            
            with col_dl1:
                st.download_button(
                    "📄 Download HTML",
                    data=st.session_state.current_website,
                    file_name=f"camped_website_{int(time.time())}.html",
                    mime="text/html"
                )
            
            with col_dl2:
                if 'current_structure' in st.session_state:
                    st.download_button(
                        "📊 Download JSON",
                        data=json.dumps(st.session_state.current_structure, indent=2),
                        file_name=f"website_structure_{int(time.time())}.json",
                        mime="application/json"
                    )
            
            with col_dl3:
                # Create a zip file with both HTML and JSON
                if st.button("📦 Download Package"):
                    st.info("💡 Use individual download buttons above")
        
        else:
            st.info("👋 Enter a website description above to generate your site!")
            
            # Show example
            with st.expander("💡 Example Descriptions"):
                examples = [
                    "A modern SaaS landing page for a project management tool with pricing tiers",
                    "Creative portfolio website for a graphic designer with project gallery",
                    "Restaurant website with menu, reservations, and location details",
                    "Tech startup page for an AI writing assistant with feature showcase",
                    "Online course platform with instructor profiles and course catalog"
                ]
                
                for example in examples:
                    if st.button(f"📝 {example[:50]}...", key=f"example_{hash(example)}"):
                        st.session_state.example_prompt = example
                        st.rerun()

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #64748b;'>
            <p>🚀 <strong>PromptPixel-You give the prompt, we paint the pixels.</strong> | Powered by Google Gemini 2.0 Flash & CampEd UI Components</p>
            <p>Built with ❤️ using Streamlit • Real-time AI Website Generation</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
