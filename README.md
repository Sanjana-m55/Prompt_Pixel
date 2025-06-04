# 🚀Prompt_Pixel-You give prompt,We give pixel

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![Gemini](https://img.shields.io/badge/Google-Gemini%202.0-orange.svg)](https://ai.google.dev)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Real-time AI-powered website generation using Google Gemini 2.0 Flash & CampEd UI Components**

Transform your ideas into beautiful, responsive websites instantly with the power of AI and modern UI components.

🎥 **[Watch Demo Video](https://youtu.be/r0p5KU4WnVw?si=rzx9sdBayBpT0eO1)**
## ✨ Features

### 🤖 AI-Powered Generation
- **Google Gemini 2.0 Flash Integration** - Advanced AI reasoning for intelligent website structure
- **Real-time Generation** - Live updates as you type with configurable delay
- **Smart Templates** - 8+ professional templates for different industries
- **Contextual Understanding** - AI analyzes requirements and suggests optimal layouts

### 🎨 Modern UI Components
- **CampEd UI Framework** - Beautiful, responsive components
- **Multiple Color Schemes** - Primary, Secondary, Accent themes
- **Advanced Styling** - Gradients, animations, hover effects
- **Mobile-First Design** - Responsive across all devices

### ⚡ Real-Time Features
- **Live Preview** - See changes instantly
- **Auto-Generation** - Triggers on content changes
- **Generation Statistics** - Track your usage
- **Settings Persistence** - Remembers your preferences

### 🛠️ Professional Tools
- **HTML Export** - Download complete websites
- **JSON Structure** - Export website configuration
- **Code Preview** - View generated HTML
- **Package Downloads** - Get everything in one go

## 🏗️ Architecture

```
Prompt Pixel:You give prompt, we give pixel
├── 🤖 Gemini AI Engine
│   ├── Structure Generation
│   ├── Content Creation
│   └── Component Selection
├── 🎨 CampEd UI System
│   ├── Component Library
│   ├── Styling Engine
│   └── Responsive Framework
├── ⚡ Real-time Engine
│   ├── Change Detection
│   ├── Auto-generation
│   └── State Management
└── 📱 Streamlit Interface
    ├── Configuration Panel
    ├── Live Preview
    └── Export System
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API Key ([Get one free](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Sanjana-m55/Prompt_Pixel
cd Prompt_Pixel
```

2. **Install dependencies**
```bash
pip install streamlit google-generativeai requests
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open your browser**
Visit `http://localhost:8501` and start creating!

### First Website

1. **Get API Key** - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Enter Key** - Paste in the sidebar configuration
3. **Choose Template** - Select from 8+ professional templates
4. **Describe Your Vision** - Write what you want to create
5. **Generate** - Watch AI build your website in real-time!

## 📋 Templates

| Template | Description | Best For |
|----------|-------------|----------|
| 🚀 **Tech Startup** | Modern SaaS landing page | Product launches, apps |
| 🎨 **Portfolio** | Creative showcase | Designers, artists |
| 🍽️ **Restaurant** | Elegant dining experience | Food businesses |
| 🛒 **E-commerce** | Online store platform | Retail, products |
| 📚 **Blog** | Content publication | Writers, content creators |
| 🏢 **Agency** | Professional services | Marketing, consulting |
| 💼 **SaaS Platform** | Software as a Service | B2B tools, platforms |
| 🎓 **Educational** | Learning platforms | Courses, training |

## ⚙️ Configuration

### API Settings
```python
# Google Gemini Configuration
GEMINI_API_KEY = "your-api-key-here"
MODEL = "gemini-2.0-flash-exp"
TEMPERATURE = 0.7  # Creativity level (0.1-1.0)
```

### UI Customization
```python
# CampEd UI Settings
COLOR_SCHEME = "primary"  # primary, secondary, accent
LAYOUT_TYPE = "default"   # default, centered, wide
REAL_TIME = True          # Enable live generation
GENERATION_DELAY = 1.0    # Seconds before auto-trigger
```

### Enhancement Options
- ✨ **Animations** - Smooth transitions and effects
- 🎨 **Icons** - Font Awesome integration
- 📱 **Mobile-First** - Responsive design priority
- 🌈 **Modern Gradients** - Contemporary visual effects
- 🖱️ **Interactive Elements** - Hover effects and micro-interactions
- ♿ **Accessibility** - WCAG compliance features

## 📊 Components Library

### Core Components
- **Button** - Primary, Secondary, Outline, Ghost variants
- **Card** - Header, content, footer with hover effects
- **Typography** - H1-H6, paragraphs, proper hierarchy
- **Navigation** - Responsive menu with brand
- **Form** - Input, textarea, select with validation

### Layout Components
- **Grid** - 2, 3, 4 column responsive layouts
- **Hero** - Large impact sections with CTAs
- **Section** - Content organization blocks
- **Container** - Max-width content wrappers

### Interactive Components
- **Modal** - Dialog overlays
- **Tabs** - Content organization
- **Progress** - Loading states
- **Alert** - Status notifications
- **Badge** - Status indicators

## 🎯 Use Cases

### 🏢 Business Websites
Generate professional business sites with contact forms, service showcases, and team profiles.

### 🛍️ E-commerce Stores
Create product catalogs, shopping features, and customer testimonials.

### 📝 Blogs & Publications
Build content-focused sites with article layouts and subscription forms.

### 🎨 Creative Portfolios
Showcase work with image galleries, project case studies, and contact information.

### 📚 Educational Platforms
Develop course catalogs, instructor profiles, and enrollment systems.

## 🔧 Advanced Usage

### Custom Prompts
```python
# Example: Advanced Restaurant Site
prompt = """
Create an upscale Italian restaurant website with:
- Hero section with signature dish image
- Menu with wine pairings
- Chef's story and philosophy
- Private dining booking system
- Events calendar
- Customer testimonials with photos
Use warm colors and elegant typography
"""
```

### API Integration
```python
# Direct API usage
generator = GeminiWebsiteGenerator(api_key)
structure = generator.generate_website_structure(
    prompt="Your website description",
    color_scheme="primary",
    layout_type="centered"
)
```

### Component Customization
```python
# Custom CampEd UI generation
ui_generator = CampEdUIGenerator()
custom_card = ui_generator.generate_card(
    title="Custom Feature",
    content="Detailed description",
    footer="Call to action"
)
```

## 📱 Responsive Design

All generated websites include:
- **Mobile-First** approach
- **Flexible Grid** system
- **Adaptive Typography** scaling
- **Touch-Friendly** interactions
- **Cross-Browser** compatibility

## 🎨 Theming System

### Color Schemes
```css
/* Primary Theme */
--camped-primary: #2563eb;
--camped-accent: #1d4ed8;

/* Secondary Theme */
--camped-primary: #64748b;
--camped-accent: #475569;

/* Accent Theme */
--camped-primary: #f59e0b;
--camped-accent: #d97706;
```

### Layout Types
- **Default** - Standard layout with sidebar
- **Centered** - Content-focused center alignment
- **Wide** - Full-width utilization

## 🚀 Performance

- **Fast Generation** - Average 3-5 seconds
- **Optimized CSS** - Minimal, efficient styles
- **CDN Integration** - Font Awesome from CDN
- **Responsive Images** - Adaptive loading
- **Clean HTML** - Semantic, accessible markup

## 🛡️ Security

- **API Key Protection** - Secure key handling
- **Input Validation** - Prompt sanitization
- **Rate Limiting** - Prevents API abuse
- **Error Handling** - Graceful failure recovery

## 📈 Analytics

Track your usage with built-in statistics:
- Generation count
- Template preferences
- Success/failure rates
- Performance metrics

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

### Development Setup
```bash
# Clone and setup
git clone https://github.com/your-username/camped-ui-generator.git
cd camped-ui-generator

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Start development server
streamlit run app.py --logger.level=debug
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini** - Powerful AI generation
- **Streamlit** - Rapid app development
- **CampEd UI** - Beautiful component system
- **Font Awesome** - Icon library
- **Community** - Feedback and contributions

## 🗺️ Roadmap

### v2.0 (Coming Soon)
- [ ] Multi-page website generation
- [ ] Database integration
- [ ] Advanced animations
- [ ] Custom component library
- [ ] Team collaboration features

### v2.1 (Future)
- [ ] WordPress export
- [ ] React component generation
- [ ] A/B testing tools
- [ ] SEO optimization
- [ ] Analytics integration

---

<div align="center">

**Built with ❤️ by the CampEd UI Team**

[⭐ Star this repo](https://github.com/Sanjana-m55/Prompt_Pixel) 

</div>
