const { Kafka } = require("kafkajs");


const topic_name = process.argv[2] || "logs2";
// const partition = process.argv[3] || 0;

createConsumer();

async function createConsumer(){
    try{
        const kafka = new Kafka({
            clientId : "kafka_ornek_1",
            brokers: ["192.168.1.112:9092"]
        });


        const consumer = kafka.consumer({
            groupId : "ornek_1_cg1"
        });

        console.log("consumer bağlanılıyor");
        await consumer.connect();
        console.log("consumer a bağlantı başarılı");

        await consumer.subscribe({
            topic:topic_name,
            fromBeginning: true
        });

        await consumer.run({
            eachMessage: async result => {
                console.log(`${result.message.value}:Partition:=>${result.partition}`)
            }
        })
    } catch(error){
        console.log("hata oluştu", error)
    }
}