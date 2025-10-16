import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class ChatbotPerformanceTest {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\chromedriver\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        
        try {
            System.out.println("=== JUDICIAL CHATBOT PERFORMANCE TEST ===");
            
            // Test page load time
            long startTime = System.currentTimeMillis();
            driver.get("https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/");
            long loadTime = System.currentTimeMillis() - startTime;
            
            System.out.println("Page load time: " + loadTime + "ms");
            
            if (loadTime < 8000) {
                System.out.println("✅ PERFORMANCE TEST PASSED: Fast loading");
            } else {
                System.out.println("⚠️ PERFORMANCE WARNING: Slow loading");
            }
            
            Thread.sleep(3000);
            
            // Test response time
            startTime = System.currentTimeMillis();
            driver.findElement(By.tagName("textarea")).sendKeys("Hello");
            long responseTime = System.currentTimeMillis() - startTime;
            
            System.out.println("UI response time: " + responseTime + "ms");
            
            if (responseTime < 2000) {
                System.out.println("✅ RESPONSIVENESS TEST PASSED: Good UI response");
            } else {
                System.out.println("⚠️ RESPONSIVENESS WARNING: Slow UI response");
            }
            
        } finally {
            driver.quit();
        }
    }
}