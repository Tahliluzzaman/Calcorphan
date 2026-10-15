
package com.calcorphan.app;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {

    private WebView calculator;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        calculator = new WebView(this);
        calculator.setWebViewClient(new WebViewClient());

        calculator.getSettings().setJavaScriptEnabled(true);
        calculator.getSettings().setDomStorageEnabled(true);

        setContentView(calculator);

        if (savedInstanceState == null) {
            calculator.loadUrl(
                "file:///android_asset/index.html"
            );
        } else {
            calculator.restoreState(savedInstanceState);
        }
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        calculator.saveState(outState);
        super.onSaveInstanceState(outState);
    }

    @Override
    public void onBackPressed() {
        if (calculator.canGoBack()) {
            calculator.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
