const puppeteer = require("puppeteer");
const fs = require("fs");
const { Parser } = require("json2csv");

(async () => {
  // Abrir navegador
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  // Búsquedas relacionadas con el aluvión en Chunchi
  const queries = [
    "deslizamiento Chunchi",
    "aluvión Chunchi",
    "inundaciones Chunchi",
    "derrumbe Chunchi"
  ];

  let allArticles = [];

  for (const query of queries) {
    console.log(`🔍 Buscando noticias para: ${query}`);

    // URL de Google Noticias
    const searchURL = `https://www.google.com/search?q=${encodeURIComponent(query)}&tbm=nws`;

    await page.goto(searchURL, { waitUntil: "load", timeout: 60000 });

    // Extraer datos
    const articles = await page.evaluate(() => {
      return Array.from(document.querySelectorAll(".SoaBEf")).map((article) => ({
        title:
          article.querySelector("div[role='heading'], h3")?.innerText.trim() ||
          "No encontrado",
        source: article.querySelector(".NUnG9d")?.innerText.trim() || "No encontrado",
        date: article.querySelector(".OSrXXb")?.innerText.trim() || "No encontrado",
        link: article.querySelector("a")?.href || "No encontrado",
      }));
    });

    allArticles = [...allArticles, ...articles];
  }

  // Cerrar navegador
  await browser.close();

  // Guardar en JSON
  fs.writeFileSync("chunchi-news.json", JSON.stringify(allArticles, null, 2), "utf-8");

  // Guardar en CSV
  const parser = new Parser();
  const csv = parser.parse(allArticles);
  fs.writeFileSync("chunchi-news.csv", csv, "utf-8");

  console.log("✅ Datos guardados en 'chunchi-news.json' y 'chunchi-news.csv'");
})();
