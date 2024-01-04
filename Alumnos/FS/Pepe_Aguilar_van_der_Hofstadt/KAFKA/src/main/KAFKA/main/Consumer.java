// se leerá las rate y se dividen en dos topics
// y se imprimen en pantalla conforme llegan

package KAFKA.main;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;

import java.time.Duration;
import java.util.Arrays;
import java.util.Properties;

public class Consumer {

    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092");
        properties.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        properties.put("value.deserializer", "KAFKA.main.RateJsonDeserializer");
        properties.put("auto.offset.reset", "earliest");
        properties.put("group.id", "reviews");

        KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(properties);

        kafkaConsumer.subscribe(Arrays.asList("reviews"));

        try {
            while (true) {
                ConsumerRecords<String, String> records = kafkaConsumer.poll(Duration.ofMillis(100));
                for (ConsumerRecord<String, String> record : records) {
                    System.out.println(String.format("Value: %s", record.value()));
                }
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        } finally {
            kafkaConsumer.close();
        }
    }
}