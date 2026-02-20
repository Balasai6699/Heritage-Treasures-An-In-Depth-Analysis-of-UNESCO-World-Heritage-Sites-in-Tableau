# Heritage Treasures: UNESCO World Heritage Sites Analysis

A comprehensive web application that explores UNESCO World Heritage Sites through interactive data visualizations created in Tableau and integrated with a Flask web framework.

Project Overview

This project provides an in-depth analysis of UNESCO World Heritage Sites (2019 dataset) through interactive visualizations, offering valuable insights into global heritage distribution, conservation status, and historical trends.

Features

### Interactive Visualizations
- **Heritage Sites by Country**: Block visualization showing site distribution by country
- **Sites at Risk**: Pie chart displaying endangered vs. safe heritage sites
- **Regional Inscription Trends**: Line chart showing historical inscription patterns by region

### Web Application
- **Responsive Dashboard**: Modern, mobile-friendly interface
- **Interactive Story**: Narrative exploration of heritage data
- **Project Documentation**: Comprehensive project information and technical details

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend**: Flask (Python)
- **Data Visualization**: Tableau Public
- **Data Source**: UNESCO World Heritage Sites 2019 Dataset

## Project Structure

```
unesco-heritage-analysis/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/
│   └── css/
│       └── style.css     # Custom styles
└── templates/
    ├── base.html         # Base template
    ├── index.html        # Home page
    ├── dashboard.html    # Dashboard page
    ├── story.html        # Story page
    └── about.html        # About page
```

##  Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**
   ```bash
   # Navigate to the project directory
   cd unesco-heritage-analysis
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

##  Application Pages

### Home Page (`/`)
- Project overview and introduction
- Quick access to dashboard and story
- Key features showcase

### Dashboard (`/dashboard`)
- Interactive Tableau dashboard embedded
- Multiple visualization types
- Real-time data exploration

### Story (`/story`)
- Narrative data story experience
- Chapter-based exploration
- Interactive navigation

### About (`/about`)
- Detailed project information
- Technical architecture
- Performance metrics

##  External Resources

- **Dataset**: [UNESCO World Heritage Sites 2019 - Kaggle](https://www.kaggle.com/datasets/ujwalkandi/unesco-world-heritage-sites/data?select=whc-sites-2019.csv)
- **Tableau Public**: [Published Dashboard & Story](https://public.tableau.com/views/UNESCOHeritage_17709235698800/Story1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

##  Key Metrics

- **1,100+** Data Points
- **8+** Interactive Visualizations
- **2** Comprehensive Dashboards
- **4** Story Scenes
- **167** Countries Represented

##  Design Features

- **Responsive Design**: Mobile-friendly interface
- **Modern UI**: Clean, professional design with Bootstrap 5
- **Interactive Elements**: Hover effects, transitions, and animations
- **Accessibility**: Semantic HTML and ARIA labels
- **Performance**: Optimized loading and smooth interactions

## Customization

### Adding New Visualizations
1. Create new visualization in Tableau
2. Publish to Tableau Public
3. Update the embed URL in the appropriate template
4. Add navigation if needed

### Styling Changes
- Modify `static/css/style.css` for custom styles
- Update Bootstrap variables in templates if needed

### Adding New Pages
1. Create new HTML template in `templates/` directory
2. Add route in `app.py`
3. Update navigation in `base.html`

##  Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Kill the process using port 5000
   # Windows:
   netstat -ano | findstr :5000
   taskkill /PID <PID> /F
   
   # macOS/Linux:
   lsof -ti:5000 | xargs kill -9
   ```

2. **Tableau embed not loading**
   - Check internet connection
   - Verify Tableau Public URL is correct
   - Ensure browser allows iframes

3. **Styling issues**
   - Clear browser cache
   - Check CSS file paths
   - Verify Bootstrap CDN links

## Development Notes

### Tableau Integration
- Uses iframe embedding for Tableau Public visualizations
- Responsive design ensures proper display on all devices
- Fullscreen mode available for better viewing experience

### Performance Considerations
- Lazy loading for images
- Optimized CSS and JavaScript
- Minimal external dependencies

### Browser Compatibility
- Chrome/Chromium: Full support
- Firefox: Full support
- Safari: Full support
- Edge: Full support
- Internet Explorer: Not supported

##  Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

##  License

This project is for educational purposes. Please refer to the original dataset and Tableau Public terms of use for data and visualization licensing.

##  Support

For questions or issues:
1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Ensure internet connectivity for Tableau embeds

---

**Project Completed**: February 2024  
**Technologies**: Flask, Tableau, Bootstrap, HTML5, CSS3  
**Dataset**: UNESCO World Heritage Sites 2019
