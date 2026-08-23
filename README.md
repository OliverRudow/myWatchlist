# myWatchList

MyWatchList is a watch list for stocks and ETFs made of different sub-lists. The application aggregates data from various sources to provide a comprehensive overview, rank assets based on custom scores, and generate exportable reports.

## Key Features & Sub-Lists

* **Static Watch List**: Contains essential information including quote names, ISIN numbers, industry, sector, and currency details.
* **Analyst Data**: Tracks expert market opinions, targets, and ratings.
* **Derivatives Information**: Holds detailed data on related options, futures, or structured products.
* **Fundamental Data**: Shows core financial metrics and company health indicators for each quote.
* **Performance Metrics**: Tracks historical returns, price changes, and volatility.

## Scoring & Reports

* **Score Rankings**: Compiles calculated score values derived from all data points into a centralized ranking list.
* **Reporting List**: A streamlined overview containing the most important information, optimized for data export.
Verwende Code mit Vorsicht.Möchtest du, dass ich noch Abschnitte für die Installation, die Technologie-Stacks oder Anwendungsbeispiele hinzufüge?KI-Antworten können Fehler enthalten. Weitere Informationen

## Project Structure

This module coordinates directly with your file utilities and shares configuration scripts:

```text
your_package/
├── __init__.py
├── myWatchListContainer                  # This module
├── myRankingWatchList                    # Holds all Score Values 
├── myReportTopList                       # Summerized Date
├── myTableSQLRankingWatchList            # Defines the SQL Data Table for the Ranking
├── myTableSQLReportTopList               # Defines the SQL Data Table for the Report Top List


## Features


## Design Configurations


## Dependencies

Ensure your execution environment has the standard data and layout processing requirements installed:

```bash
pip install reportlab
```

## Quick Start

Initialize `myInvestments` by setting an active working directory and defining your target output filename:

## Module Overview

### Classes

### Layout Triggers

## License & Copyright

© 2026, Brain Center Höfen. All rights reserved.  
**Author:** Oliver Rudow (<oliver.rudow@googlemail.com>)  
**Version:** 0.1.0
