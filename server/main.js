Meteor.startup(function () {
    console.log('we start');
    if (mobj.find().count() === 0) {
        console.log('collection mobj is empty');
        let i=0;
        for(i;i<objects.length;i++){
            mobj.insert(objects[i]);
        }
    }
});