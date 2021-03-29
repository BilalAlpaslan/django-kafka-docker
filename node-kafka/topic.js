const { Kafka } = require("kafkajs");

createTopic();


async function createTopic(){
    try{
        const kafka = new Kafka({
            clientId : "kafka_ornek_1",
            brokers: ["192.168.1.112:9092"]
        });


        const admin = kafka.admin();
        console.log("kafka broker a bağlanılıyor");
        await admin.connect();
        console.log("kafka broker a bağlantı başarılı,topic üretiliyo");
        await admin.createTopics({
            topics : [
                {
                    topic : "logs",
                    numPartitions: 1
                },
                {
                    topic : "logs2",
                    numPartitions: 2
                }
            ]
        });
        console.log("topic oluşturuldu");
        await admin.disconnect();
    } catch(error){
        console.log("hata oluştu", error)
    } finally {
        process.exit(0);
    }
}