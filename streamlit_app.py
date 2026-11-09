
package com.example.zikriman

import android.app.Activity
import android.app.WallpaperManager
import android.content.ComponentName
import android.content.Intent
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.widget.*

class MainActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val layout = LinearLayout(this)
        layout.orientation = LinearLayout.VERTICAL
        layout.gravity = Gravity.CENTER
        layout.setPadding(25, 40, 25, 40)
        layout.setBackgroundColor(Color.rgb(8, 43, 34))

        val title = TextView(this)
        title.text = "زیکری من"
        title.textSize = 35f
        title.setTextColor(Color.rgb(230, 190, 100))
        title.gravity = Gravity.CENTER

        val dua = TextView(this)
        dua.text = "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ"
        dua.textSize = 28f
        dua.setTextColor(Color.WHITE)
        dua.gravity = Gravity.CENTER

        val translation = TextView(this)
        translation.text = "پاک و بێگەردە خودا، ستایش بۆ ئەوە"
        translation.textSize = 20f
        translation.setTextColor(Color.LTGRAY)
        translation.gravity = Gravity.CENTER

        val button = Button(this)
        button.text = "دانانی زیکر لە شاشەی قفڵ"

        button.setOnClickListener {
            val intent = Intent(
                WallpaperManager.ACTION_CHANGE_LIVE_WALLPAPER
            )
            intent.putExtra(
                WallpaperManager.EXTRA_LIVE_WALLPAPER_COMPONENT,
                ComponentName(
                    this,
                    DhikrWallpaperService::class.java
                )
            )
            startActivity(intent)
        }

        layout.addView(title)
        layout.addView(dua)
        layout.addView(translation)
        layout.addView(button)

        setContentView(layout)
    }
}
package com.example.zikriman

import android.service.wallpaper.WallpaperService
import android.graphics.Canvas
import android.graphics.Paint
import android.graphics.Color
import android.view.SurfaceHolder
import android.os.Handler
import android.os.Looper

class DhikrWallpaperService : WallpaperService() {

    override fun onCreateEngine(): Engine {
        return DhikrEngine()
    }

    inner class DhikrEngine : Engine() {

        private val handler = Handler(Looper.getMainLooper())

        private val duas = listOf(
            "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ",
            "أَسْتَغْفِرُ اللَّهَ",
            "لَا إِلَهَ إِلَّا اللَّهُ",
            "الْحَمْدُ لِلَّهِ",
            "اللَّهُ أَكْبَرُ",
            "سُبْحَانَ اللَّهِ",
            "رَبِّ اغْفِرْ لِي وَارْحَمْنِي"
        )

        private var index = 0
        private var visible = false

        private val paint = Paint(Paint.ANTI_ALIAS_FLAG)

        private val update = object : Runnable {
            override fun run() {
                if (!visible) return

                index = (index + 1) % duas.size
                drawDua()

                handler.postDelayed(this, 60000)
            }
        }

        override fun onVisibilityChanged(v: Boolean) {
            visible = v
            handler.removeCallbacks(update)

            if (visible) {
                drawDua()
                handler.postDelayed(update, 60000)
            }
        }

        override fun onSurfaceChanged(
            holder: SurfaceHolder,
            format: Int,
            width: Int,
            height: Int
        ) {
            drawDua()
        }

        override fun onSurfaceDestroyed(holder: SurfaceHolder) {
            visible = false
            handler.removeCallbacks(update)
            super.onSurfaceDestroyed(holder)
        }

        private fun drawDua() {
            val canvas: Canvas =
                surfaceHolder.lockCanvas() ?: return

            try {
                canvas.drawColor(Color.rgb(8, 43, 34))

                paint.color = Color.rgb(230, 190, 100)
                paint.textSize = 48f
                paint.textAlign = Paint.Align.CENTER

                canvas.drawText(
                    "زیکری من",
                    canvas.width / 2f,
                    canvas.height * 0.30f,
                    paint
                )

                paint.color = Color.WHITE
                paint.textSize = 52f

                canvas.drawText(
                    duas[index],
                    canvas.width / 2f,
                    canvas.height * 0.50f,
                    paint
                )

            } finally {
                surfaceHolder.unlockCanvasAndPost(canvas)
            }
        }
    }
}
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <application
        android:theme="@android:style/Theme.Material.Light.NoActionBar"
        android:label="زیکری من">

        <activity
            android:name=".MainActivity"
            android:exported="true">

            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>

        </activity>

        <service
            android:name=".DhikrWallpaperService"
            android:permission="android.permission.BIND_WALLPAPER"
            android:exported="true">

            <intent-filter>
                <action android:name="android.service.wallpaper.WallpaperService"/>
            </intent-filter>

            <meta-data
                android:name="android.service.wallpaper"
                android:resource="@xml/dhikr_wallpaper"/>

        </service>

    </application>
</manifest>
<wallpaper xmlns:android="http://schemas.android.com/apk/res/android"
    android:description="@string/app_name" />
