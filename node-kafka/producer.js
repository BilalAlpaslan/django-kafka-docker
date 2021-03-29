const { Kafka } = require("kafkajs");

const topic_name = process.argv[2] || "logs2";
const partition = process.argv[3] || 0;

createProducer();

async function createProducer(){
    try{
        const kafka = new Kafka({
            clientId : "kafka_ornek_1",
            brokers: ["192.168.1.112:9092"]
        });


        const producer = kafka.producer();
        console.log("producer a bağlanılıyor");
        await producer.connect();
        console.log("producer a bağlantı başarılı");
        const message_result = await producer.send({
            topic:topic_name,
            messages: [
                {
                    value:"bu bir test log mesajıdır",
                    partition : partition
                }
            ]
        });
        console.log("gönderim başarılı",JSON.stringify(message_result))
        await producer.disconnect();
    } catch(error){
        console.log("hata oluştu", error)
    } finally {
        process.exit(0);
    }
}