package com.example.moretech

import android.view.LayoutInflater
import com.yandex.mapkit.geometry.Point
import com.yandex.mapkit.map.MapObject
import com.yandex.mapkit.map.MapObjectTapListener
import com.yandex.mapkit.map.PlacemarkMapObject

class MyMapObjectTapListener// : MapObjectTapListener {
//    override fun onMapObjectTap(p0: MapObject, p1: Point): Boolean {
//        if (p0 is PlacemarkMapObject) {
//            val place = p0.userData as Place
//            showInfoCard(place)
//            return true
//        }
//        return false
//    }
//    private fun showInfoCard(place: Place) {
//        val dialogView = LayoutInflater.from(context).inflate(R.layout.marker_info_contents, null)
//        val nameTextView = dialogView.findViewById<TextView>(R.id.nameTextView)
//        val addressTextView = dialogView.findViewById<TextView>(R.id.addressTextView)
//        val ratingTextView = dialogView.findViewById<TextView>(R.id.ratingTextView)
//
//        nameTextView.text = place.name
//        addressTextView.text = place.address
//        ratingTextView.text = place.rating.toString()
//
//        // Show the dialog with the information card
//        // You can use AlertDialog, DialogFragment, or any other dialog implementation
//
//        // Example using AlertDialog:
//        val dialogBuilder = AlertDialog.Builder(context)
//            .setView(dialogView)
//            .setPositiveButton("OK") { dialog, _ ->
//                dialog.dismiss()
//            }
//        val dialog = dialogBuilder.create()
//        dialog.show()
//    }
