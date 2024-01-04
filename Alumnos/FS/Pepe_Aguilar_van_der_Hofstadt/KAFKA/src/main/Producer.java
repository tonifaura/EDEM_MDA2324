// Aqui producira la rate al mismo topic
//
package KAFKA.main;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;
import java.util.Random;

public class Producer {
    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092");
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);

        Random random = new Random();

        try {
            for (int i = 0; i < 100; i++) {
                // Simulación de reseñas aleatorias para restaurantes
               // String restaurant = restaurants[random.nextInt(restaurants.length)];
                int option = random.nextInt(2);
                String business = "";
                if(option == 0){
                    business = "Restaurant";
                }
                else{
                    business = "Hotel";
                }
                String review = "Review for " + business + ": Rating - " + (random.nextInt(5) + 1);

                // Enviar reseña al tema "restaurant-reviews"
                producer.send(new ProducerRecord<>("reviews", review));

                Thread.sleep(100); // Esperar un breve periodo de tiempo entre reseñas
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            producer.close();
        }
    }
}