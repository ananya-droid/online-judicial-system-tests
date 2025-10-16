import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class ChatbotFunctionalTest {
    public static void main(String[] args) throws InterruptedException {
        // Update this path for your Eclipse
        System.setProperty("webdriver.chrome.driver", "C:\\chromedriver\\chromedriver.exe");
        
        WebDriver driver = new ChromeDriver();
        
        try {
            System.out.println("=== JUDICIAL CHATBOT FUNCTIONAL TEST ===");
            
            // 1. Open your chatbot
            driver.get("https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/");
            driver.manage().window().maximize();
            Thread.sleep(5000);
            
            System.out.println("Page opened: " + driver.getTitle());
            
            // 2. Handle wake-up if needed
            try {
                WebElement wakeBtn = driver.findElement(By.xpath("//button[contains(., 'Yes, get this app back up')]"));
                wakeBtn.click();
                System.out.println("Wake-up button clicked");
                Thread.sleep(3000);
            } catch (Exception e) {
                System.out.println("No wake-up needed");
            }
            
            // 3. Find input and send legal query
            WebElement input = driver.findElement(By.tagName("textarea"));
            String query = "How to file a consumer complaint?";
            input.sendKeys(query);
            input.submit();
            
            System.out.println("Query sent: " + query);
            
            // 4. Wait for response
            Thread.sleep(5000);
            
            // 5. Check response
            String pageText = driver.findElement(By.tagName("body")).getText();
            if (pageText.toLowerCase().contains("consumer") || 
                pageText.toLowerCase().contains("complaint") || 
                pageText.toLowerCase().contains("file")) {
                System.out.println("✅ FUNCTIONAL TEST PASSED: Chatbot provided relevant legal guidance");
            } else {
                System.out.println("❌ FUNCTIONAL TEST FAILED: No relevant response found");
            }
            
        } catch (Exception e) {
            System.out.println("❌ TEST ERROR: " + e.getMessage());
        } finally {
            driver.quit();
            System.out.println("Browser closed");
        }
    }
}