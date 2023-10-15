package com.example.moretech

import android.Manifest
import android.app.Dialog
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.widget.SwitchCompat
import androidx.cardview.widget.CardView
import androidx.core.app.ActivityCompat
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.moretech.databinding.ActivityMapBinding
import com.example.moretech.models.FilterOfficeResponse
import com.example.moretech.models.InfoCard
import com.example.moretech.models.OfficesModel
import com.example.moretech.viewmodels.DepartsViewModel
import com.yandex.mapkit.Animation
import com.yandex.mapkit.MapKit
import com.yandex.mapkit.MapKitFactory
import com.yandex.mapkit.directions.DirectionsFactory
import com.yandex.mapkit.directions.driving.VehicleOptions
import com.yandex.mapkit.geometry.Point
import com.yandex.mapkit.map.Map
import com.yandex.mapkit.map.MapObject
import com.yandex.mapkit.map.MapObjectCollection
import com.yandex.mapkit.map.MapObjectTapListener
import com.yandex.mapkit.map.PlacemarkMapObject
import com.yandex.mapkit.mapview.MapView
import com.yandex.mapkit.transport.TransportFactory
import com.yandex.runtime.image.ImageProvider

class MapActivity : AppCompatActivity(), CardLogic.CardInteractionListener {
    val MY_API_KEY = "e0d3c4fd-81d1-4328-8efb-3c7d4f5600ef"

    lateinit var map: Map
    lateinit var mapview: MapView
    lateinit var collection: MapObjectCollection
    lateinit var departsViewModel: DepartsViewModel
    lateinit var btnList: Button
    lateinit var adapter: ListViewAdapter
    lateinit var btn_sort: Button
    lateinit var binding: ActivityMapBinding
    lateinit var recyclerView: RecyclerView
    private var dialog1: Dialog? = null
    private val cardLogic = CardLogic()



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        MapKitFactory.setApiKey("e0d3c4fd-81d1-4328-8efb-3c7d4f5600ef")
        MapKitFactory.initialize(this)
        setContentView(R.layout.activity_map)


        dialog1 = Dialog(this, R.style.CardDialog)
        dialog1?.setContentView(R.layout.filter_card)

        cardLogic.initializeViews(dialog1!!)
        cardLogic.setCardInteractionListener(this)

        //dialog?.window?.setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))

        departsViewModel = ViewModelProvider(this)[DepartsViewModel::class.java]
        binding = ActivityMapBinding.inflate(layoutInflater)
        btn_sort = findViewById(R.id.btn_sort)
        recyclerView = findViewById(R.id.info_list)

        initRecycleView()
        mapview = findViewById(R.id.mapview)
        btnList = findViewById(R.id.btn_list)
        map = mapview.mapWindow.map

        val pedestrianRouter = TransportFactory.getInstance().createPedestrianRouter()


        btnList.setOnClickListener {
            if (recyclerView.visibility == View.GONE) {
                recyclerView.visibility = View.VISIBLE
            } else {
                recyclerView.visibility = View.GONE
            }
        }



        requestLocationPermission()
        Animation(Animation.Type.SMOOTH, 10f)
        var mapKit: MapKit = MapKitFactory.getInstance()


        var probki = mapKit.createTrafficLayer(mapview.mapWindow)
        var location = mapKit.createUserLocationLayer(mapview.mapWindow)

        val atmsCollection = map.mapObjects.addCollection()
        val officesCollection = map.mapObjects.addCollection()
        departsViewModel.recieveDepartsInfo()
        departsViewModel.recieveOfficesInfo()

//        departsViewModel.atmData.observe(this@MapActivity) {  list ->
//            atmsCollection.clear()
//            val addlist: ArrayList<InfoCard> = ArrayList()
//            for(i in 1..list.atms.size){
//                val latitude = list.atms[i]["latitude"] as Double
//                val longitude = list.atms[i]["longitude"] as Double
//
//                val placemarkMapObject = atmsCollection.addPlacemark().apply {
//                    geometry = Point(latitude, longitude)
//                    setIcon(ImageProvider.fromResource(this@MapActivity, R.drawable.ic_pin))
//                    addTapListener(MapObjectTapListener { mapObject, point ->
//                        val latitude = point.latitude
//                        val longitude = point.longitude
//                        Toast.makeText(this@MapActivity, "$latitude, $longitude", Toast.LENGTH_SHORT).show()
//                        true
//                    })
//                }
//            }
//        }
        atmsCollection.addTapListener { _, point ->
            val latitude = point.latitude
            val longitude = point.longitude
            Toast.makeText(this@MapActivity, "$latitude, $longitude", Toast.LENGTH_SHORT).show()
            true
        }


        departsViewModel.officeData.observe(this@MapActivity) {  list ->
            Toast.makeText(this@MapActivity, "${list.offices[1]["id"]}", Toast.LENGTH_LONG).show()
            val addlist: ArrayList<InfoCard> = ArrayList()
            for(i in 1..list.offices.size){
                addlist.add(InfoCard(list.offices[i]["salepoint_name"].toString(), list.offices[i]["adress"].toString()))
                val latitude = list.offices[i]["latitude"] as Double
                val longitude = list.offices[i]["longitude"] as Double
                officesCollection.addPlacemark().apply {
                    geometry = Point(latitude, longitude)
                    setIcon(ImageProvider.fromResource(this@MapActivity, R.drawable.ic_pin))
                    userData = list.offices[i]["id"]

                }
            }
        }



        officesCollection.addTapListener { placeMark, point ->
            val latitude = point.latitude
            val longitude = point.longitude
            val cardView: CardView = findViewById(R.id.info_card)

            // Set CardView to visible
            cardView.visibility = View.VISIBLE

            true
        }



        btn_sort.setOnClickListener {
            // Create the dialog
            //dialog = Dialog(this, R.style.CardDialog)
            //dialog?.setContentView(R.layout.filter_card)
            //officesCollection.clear()
            departsViewModel._officeData = MutableLiveData<OfficesModel>()
            dialog1?.show()
        }




        departsViewModel.error.observe(this) { errorMessage ->
                Toast.makeText(this, errorMessage, Toast.LENGTH_SHORT).show()
                val intent = Intent(this, MapActivity::class.java)
                //startActivity(intent)
        }

        location.isVisible = true
        atmsCollection.isVisible = true
        map.mapObjects.isVisible = true
    }

    private fun requestLocationPermission(){
        if(ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED
            && (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M)){
            requestPermissions(arrayOf(Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION), 99)
        }
    }

    private fun initRecycleView() = with(binding){
        adapter = ListViewAdapter()
        recyclerView.layoutManager= LinearLayoutManager(this@MapActivity)
        recyclerView.adapter = adapter
    }

    override fun onStart() {
        mapview.onStart()
        MapKitFactory.getInstance().onStart()
        super.onStart()
    }

    override fun onStop() {
        mapview.onStop()
        MapKitFactory.getInstance().onStop()
        super.onStop()
    }





    override fun onOptionsSelected(options: FilterOfficeResponse) {
        departsViewModel.updateOfficesInfo(options)
        Toast.makeText(this@MapActivity, "$options", Toast.LENGTH_SHORT).show()
    }

}
