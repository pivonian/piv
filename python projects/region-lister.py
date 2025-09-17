europe_countries = [
    "Russia",
    "Germany",
    "Turkey",
    "France",
    "United Kingdom",
    "Italy",
    "Spain",
    "Ukraine",
    "Poland",
    "Romania",
    "Netherlands",
    "Belgium",
    "Czechia",
    "Greece",
    "Portugal",
    "Sweden",
    "Hungary",
    "Belarus",
    "Austria",
    "Serbia",
    "Switzerland",
    "Bulgaria",
    "Denmark",
    "Finland",
    "Slovakia",
    "Norway",
    "Ireland",
    "Croatia",
    "Moldova",
    "Bosnia and Herzegovina",
    "Albania",
    "Lithuania",
    "North Macedonia",
    "Slovenia",
    "Latvia",
    "Estonia",
    "Montenegro",
    "Luxembourg",
    "Malta",
    "Iceland",
    "Andorra",
    "Monaco",
    "Liechtenstein",
    "San Marino",
    "Vatican City"
]

asia_countries = [
    "China",
    "India",
    "Indonesia",
    "Pakistan",
    "Bangladesh",
    "Japan",
    "Philippines",
    "Vietnam",
    "Turkey",
    "Iran",
    "Thailand",
    "Myanmar",
    "South Korea",
    "Iraq",
    "Afghanistan",
    "Saudi Arabia",
    "Uzbekistan",
    "Malaysia",
    "Yemen",
    "Nepal",
    "North Korea",
    "Sri Lanka",
    "Kazakhstan",
    "Syria",
    "Cambodia",
    "Jordan",
    "Azerbaijan",
    "United Arab Emirates",
    "Tajikistan",
    "Israel",
    "Laos",
    "Lebanon",
    "Kyrgyzstan",
    "Singapore",
    "Oman",
    "Palestine",
    "Kuwait",
    "Georgia",
    "Mongolia",
    "Armenia",
    "Qatar",
    "Bahrain",
    "Timor-Leste",
    "Cyprus",
    "Bhutan",
    "Maldives"
]

africa_countries = [
    "Nigeria",
    "Ethiopia",
    "Egypt",
    "DR Congo",
    "Tanzania",
    "South Africa",
    "Kenya",
    "Uganda",
    "Algeria",
    "Sudan",
    "Morocco",
    "Angola",
    "Mozambique",
    "Ghana",
    "Madagascar",
    "Cameroon",
    "Côte d'Ivoire",
    "Niger",
    "Burkina Faso",
    "Mali",
    "Malawi",
    "Zambia",
    "Senegal",
    "Chad",
    "Somalia",
    "Zimbabwe",
    "Guinea",
    "Rwanda",
    "Benin",
    "Burundi",
    "Tunisia",
    "South Sudan",
    "Togo",
    "Sierra Leone",
    "Libya",
    "Congo",
    "Liberia",
    "Central African Republic",
    "Mauritania",
    "Eritrea",
    "Namibia",
    "Gambia",
    "Botswana",
    "Gabon",
    "Lesotho",
    "Guinea-Bissau",
    "Equatorial Guinea",
    "Mauritius",
    "Eswatini",
    "Djibouti",
    "Comoros",
    "Cabo Verde",
    "Sao Tome and Principe",
    "Seychelles"
]

north_america_countries = [
    "United States",
    "Mexico",
    "Canada",
    "Guatemala",
    "Cuba",
    "Haiti",
    "Dominican Republic",
    "Honduras",
    "El Salvador",
    "Nicaragua",
    "Costa Rica",
    "Panama",
    "Jamaica",
    "Trinidad and Tobago",
    "Belize",
    "Bahamas",
    "Barbados",
    "Saint Lucia",
    "Grenada",
    "Saint Vincent and the Grenadines",
    "Antigua and Barbuda",
    "Saint Kitts and Nevis"
]

south_america_countries = [
    "Brazil",
    "Colombia",
    "Argentina",
    "Peru",
    "Venezuela",
    "Chile",
    "Ecuador",
    "Bolivia",
    "Paraguay",
    "Uruguay",
    "Guyana",
    "Suriname"
]

oceania_countries = [
    "Australia",
    "Papua New Guinea",
    "New Zealand",
    "Fiji",
    "Solomon Islands",
    "Micronesia",
    "Vanuatu",
    "Samoa",
    "Kiribati",
    "Tonga",
    "Marshall Islands",
    "Palau",
    "Tuvalu",
    "Nauru"
]

middle_east_countries = [
    "Egypt",
    "Iran",
    "Turkey",
    "Iraq",
    "Saudi Arabia",
    "Yemen",
    "Syria",
    "United Arab Emirates",
    "Israel",
    "Jordan",
    "Lebanon",
    "Oman",
    "Kuwait",
    "Qatar",
    "Bahrain",
    "Palestine"
]

region = input('Input a region: ').strip()

if region.lower() == 'middle east':
    for country in middle_east_countries:
        print(country)
elif region.lower() in ['oceania', 'australasia', 'australia', 'pacific islands']:
    for country in oceania_countries:
        print(country)
elif region.lower() == 'north america':
    for country in north_america_countries:
        print(country)
elif region.lower() == 'south america':
    for country in south_america_countries:
        print(country)
elif region.lower() in ['america', 'americas']:
    for country in north_america_countries:
        print(country)
    for country in south_america_countries:
        print(country)
elif region.lower() == 'asia':
    for country in asia_countries:
        print(country)
elif region.lower() == 'eurasia':
    for country in europe_countries:
        print(country)
    for country in asia_countries:
        print(country)
elif region.lower() == 'europe':
    for country in europe_countries:
        print(country)
elif region.lower() == 'africa':
    for country in africa_countries:
        print(country)