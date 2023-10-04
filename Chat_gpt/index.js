// Crea un bot de Discord utilizando la API de OpenAI que interactúa en el servidor de Discord
require('dotenv').config();

// Prepara la conexión a Discord
const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
]});

// Prepara la conexión a la API de OpenAI
const { Configuration, OpenAIApi } = require('openai');
const configuration =  new Configuration({
    organization: process.env.OPENAI_ORG,
    apiKey: process.env.OPENAI_KEY,
});
const openai = new OpenAIApi(configuration);

// ID del canal donde el bot responderá automáticamente
const channelId = '1106363265157697579'; // Reemplaza con la ID de tu canal

// Verifica cuando se envía un mensaje en Discord
client.on('messageCreate', async function(message) {
    try {
        // No responda a mensajes propios o de otros bots
        if (message.author.bot) return;

        // Verifica si el mensaje se envió en el canal deseado
        if (message.channel.id !== channelId) return;

        // Elimina las menciones y espacios en blanco del mensaje para obtener la consulta
        const query = message.content.replace(/<@!?(\d+)>/g, '').trim();

        // Verifica si el mensaje no está vacío
        if (query.length === 0) return;

        const gptResponse = await openai.createCompletion({
            model: "text-davinci-003", // Cambiado a text-davinci-003 para una respuesta más coherente
            prompt: `ChatGPT es un chatbot amigable.\n\
ChatGPT: ¡Hola! ¿Cómo estás?\n\
${message.author.username}: ${query}\n\
ChatGPT:`,
            temperature: 0.7, // Reducido para generar respuestas más coherentes
            max_tokens: 200,
            stop: ["\n"], // Detiene la generación después de un salto de línea
            n: 1, // Genera una sola respuesta para evitar respuestas aleatorias
        });

        // Extrae la respuesta generada por GPT-3
        const response = gptResponse.data.choices[0].text.trim();

        // Envía la respuesta al canal de Discord
        message.channel.send(response);

    } catch (err) {
        console.log(err);
    }
});

// Inicia sesión del bot en Discord
client.login(process.env.DISCORD_TOKEN);
console.log("El bot de ChatGPT ahora está conectado");